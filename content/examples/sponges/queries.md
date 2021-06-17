---
title: "Finding HMA-LMA subgraphs"
description: ""
lead: ""
date: 2021-05-07T10:49:49+02:00
lastmod: 2021-05-07T10:49:49+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Sponges"
weight: 103
toc: true
---
Find all Python code used on this page here: <a href="https://ramellose.github.io/mako_docs/demo/sponge_queries.py">sponge_queries.py</a><br>

With all networks and the HMA-LMA links available via the Neo4j database, we can start considering associations that could be linked to HMA-LMA status. For example, we might try to recover all associations between taxa that are both associated to HMA status in some way, with the query below:

<pre><code>
MATCH p=(:Type {name: 'HMA'})--()--(:Taxon)--(:Edge)--(:Taxon)--()--(:Type {name: 'HMA'}) RETURN p LIMIT 25
</pre></code>

This query first matches the HMA node and then passes through either a <code>Class</code> or <code>Phylum</code> node to connect to an association, which should similarly be connected to the HMA node. 

If we want to export the subgraph of HMA and LMA associations to Cytoscape, we can adapt the above query to connect associations to a new network node. The easiest way to do this, is via the mako API, which you can access via a Python interpreter. For instructions on starting the interpreter, please see the <a href="https://ramellose.github.io/mako_docs/manual/api/python/">API section of the manual</a>.  Make sure to adjust the driver configuration settings for your instance of Neo4j. 


<pre><code>
from mako.scripts.io import IoDriver
import os

loc = os.getcwd() 

driver = IoDriver(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=loc,
                  encrypted=False)

driver.write("MERGE (n:Network {name: 'HMA_network'}) RETURN n")

hma_query = "MATCH p=(:Type {name: 'HMA'})--()--" \
            "(:Taxon)--(a:Edge)--(:Taxon)--()--(:Type {name: 'HMA'}) RETURN a"
results = driver.query(hma_query)
</pre></code>

First, the driver is used to create a HMA <code>Network</code> node. The query after that returns all <code>Edge</code>nodes that are linked to HMA status in these sponges. The query below takes the names of these nodes and connects them to the HMA node. 

<pre><code>
edge_names = [{"name": x['a']['name']} for x in results]
query = "WITH $batch as batch " \
        "UNWIND batch as record " \
        "MATCH (a:Edge {name:record.name}), (b:Network {name: 'HMA_network'})" \
        "MERGE (a)-[r:PART_OF]-(b) RETURN r"
driver.write(query, batch=edge_names)
</pre></code>

We can repeat the above queries for the LMA status. 

<pre><code>
driver.write("MERGE (n:Network {name: 'LMA_network'}) RETURN n")

lma_query = "MATCH p=(:Type {name: 'LMA'})--()--" \
            "(:Taxon)--(a:Edge)--(:Taxon)--()--(:Type {name: 'LMA'}) RETURN a"
results = driver.query(lma_query)

edge_names = [{"name": x['a']['name']} for x in results]
query = "WITH $batch as batch " \
        "UNWIND batch as record " \
        "MATCH (a:Edge {name:record.name}), (b:Network {name: 'LMA_network'})" \
        "MERGE (a)-[r:PART_OF]-(b) RETURN r"
driver.write(query, batch=edge_names)
</pre></code>

Finally, we can export these two networks to a running instance of Cytoscape. 

<pre><code>
driver.export_cyto(networks=['HMA_network', 'LMA_network'])
</pre></code>

With Cytoscape, it is possible to format networks based on specific properties (Figure 2). Indeed, it becomes possible to see that most associations in the LMA network are Gammaproteobacteria (shown in yellow). Additionally, the mako export includes information like the number of source networks that contained these associations; although not shown below, it looks like most associations between taxa linked to LMA status only occur in one of the sponge networks, rather than in multiple of them. 

<figure>
  <img src="/images/sponge_network.PNG" alt="Network with associations linked to LMA status in sponges. Negatively-weighted associations are shown in blue, positively-weighted ones in red." width="600"> 
  <figcaption>Figure 2: Network with associations linked to LMA status in sponges. Negatively-weighted associations are shown in blue, positively-weighted ones in red.</figcaption>
</figure>