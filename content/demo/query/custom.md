---
title: "Writing custom queries"
description: ""
lead: ""
date: 2021-04-28T13:57:41+02:00
lastmod: 2021-04-28T13:57:41+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Custom queries"
weight: 3
toc: true
---

All of mako's driver classes are able to use the functions that call custom queries, so there is no need to close and recreate the driver to use these functions; however, for the sake of simplicity, the code below calls the <code>ParentDriver</code> class. 

First, we need to start up the driver and connect to the database. 
<pre><code>
from mako.scripts.utils import ParentDriver

driver = ParentDriver(uri='neo4j://localhost:7688',
                      user='neo4j',
                      password='test',
                      filepath=filepath,
                      encrypted=False)
</pre></code>

The <code>ParentDriver</code> only has three class methods: <code>close</code>, <code>query</code> and <code>write</code>. The <code>close</code> method closes the connection to the Neo4j database. There is no need to run this every time you run a query, but it can be helpful to include it in a script so you are not opening many connections at a time. The <code>query</code> processes a read transaction, while the <code>write</code> processes a write transaction. Both of these methods require a Cypher query as input, but only the <code>write</code> method can make changes to the database. 

Let's first take a look at the structure of some simple query results. 
We will use this query: <br>
<code>MATCH p=(:Genus {name: 'g__Escherichia'})--(:Taxon)--(:Edge) RETURN p</code>
<br><br>

The query returns a pattern <code>p</code>, which consists of a <code>Genus</code> node, a <code>Taxon</code> node and an <code>Edge</code> node. When we run the query, we will get a list of all results; the section below shows our first result. 

<pre><code>
query = "MATCH p=(:Genus {name: 'g__Odoribacter'})--(:Taxon)--(:Edge) RETURN p"
query_results = driver.query(query)

print(len(query_results))
print(query_results[0])

10
{'p': [{'name': 'g__Odoribacter'}, 
        'MEMBER_OF', 
        {'name': '11947-agglom-107'}, 
        'PARTICIPATES_IN', 
        {'name': '7c942282-a6f1-4d38-b7e0-8ac3d89f69b1', 'weight': -0.30529758442530924}]}
</pre></code>

We can see that the query result is returned as a dictionary, with each value (in this case only <code>p</code>) as a key in the dictionary. The value is a list, with each item in the list representing an item in the path. Nodes are returned as dictionaries, the other values are relationship labels. 

To access values in the query, it can be helpful to process them. Neo4j does not keep track of the "direction" of the pattern matching; if a pattern matches the same three nodes in two ways (e.g. A--B--C and C--B--A), both matches will be returned as results. When studying motifs, it is therefore crucial to filter out these duplicates. 

The script below does exactly this: it first makes a list of lists, with each sublist containing all node names (not relationships) in each pattern. The sublists are then sorted. Next, the set of each sublist is taken, so that they only contain unique nodes. For this query, this step is not actually necessary, but for loops like (A--B--C--A) it makes sure that we do not return (B--C--A--B) too. Finally, we return only unique sublists. 

<code><pre>
all_nodes = [[y['name'] for y in x['p'] if type(y) == dict] for x in query_results]
for y in all_nodes:
    y.sort()
all_nodes = [set(x) for x in all_nodes]
all_nodes = set(map(tuple, all_nodes))
</code></pre>

Note that, if we change the query, we may need to change our queries to go along with this. For example, we can choose to return the genus assignment of the association partners rather than the pattern above. There is no need to specify the <code>Taxon</code> nodes, since the only connection between <code>Genus</code> and <code>Edge</code> nodes is via taxa. 

<code><pre>
query = "MATCH (:Genus {name: 'g__Odoribacter'})--()--(:Edge)--()--(n:Genus) RETURN n"
query_results = driver.query(query)

print(len(query_results))
print(query_results[0])

8
{'n': {'name': 'g__[Ruminococcus]'}}
</code></pre>

We actually have fewer matches than before. Apparently, not all associations are with taxa that have a genus assignment. Morever, we can see that the structure of the results is the same; we get a dictionary that has a key identical to the parameter in our Cypher <code>RETURN</code> and a value that is a node dictionary. 

If we are interested in finding those associations without a genus assignment, we can actually add this to the query. The <code>WHERE NOT</code> clause states that the node <code>n</code> cannot have a link to a <code>Genus</code>, while the <code>WITH</code> clause then uses this node to return the pattern matching the <code>Family</code> node. 

<code><pre>
query = "MATCH (:Genus {name: 'g__Odoribacter'})--()--(:Edge)--(n) 
         WHERE NOT (n)--(:Genus) 
         WITH n MATCH p=(n)--(:Family) RETURN p"
query_results = driver.query(query)

print(len(query_results))
print(query_results[0])

2
{'p': [{'name': '11947-agglom-78'}, 'MEMBER_OF', {'name': 'f__[Barnesiellaceae]'}]}
</code></pre>

Finally, it is also possible that we may have specified a query that is technically correct, but the pattern does not match to any data in the database. For example, <code>Genus</code> nodes can only connect to <code>Taxon</code> nodes, and <code>Taxon</code> nodes cannot directly connect to a <code>Network</code> node. In this case, the query results are just an empty list.

<code><pre>
query = "MATCH p=(:Genus {name: 'g__Odoribacter'})--()--(:Network) RETURN p"
query_results = driver.query(query)

print(query_results)

[]
</code></pre>