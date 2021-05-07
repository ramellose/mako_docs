---
title: "Clauses"
description: ""
lead: ""
date: 2021-05-07T17:22:58+02:00
lastmod: 2021-05-07T17:22:58+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Basics"
weight: 2
toc: true
---

In a Cypher query, clauses state what needs to happen with the pattern specified after the clause. For an exhaustive list of clauses, we refer to <a href="https://neo4j.com/docs/cypher-manual/current/clauses/">the Neo4j Cypher manual</a>. Here, we will explain what a clause looks like and what the most common clauses do.  

In the Cypher queries below, <code>MATCH</code>, <code>RETURN</code> and <code>LIMIT</code> are all clauses. While it is not mandatory to use capital letters, we usually do this for clarity so that it becomes easier to see which parts of the Cypher query are clauses. 

<code>MATCH (n) RETURN n LIMIT 25</code>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MATCH</code></b><br>
The <code>MATCH</code> clause finds the pattern described after the clause. In the example above, the <code>MATCH</code> clause will find any node n. 
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>RETURN</code></b><br>
The <code>RETURN</code> clause returns the pattern described after the clause. In the example above, the <code>RETURN</code> clause will return the previously identified node n. 
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>LIMIT</code></b><br>
The <code>LIMIT</code> clause limits the number of returned results. In the example above, the <code>LIMIT</code> clause will ensure that no more than 25 nodes are returned. 
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>CREATE</code></b><br>
The <code>CREATE</code> clause creates a node or a relationship. In the following examples, the <code>CREATE</code> clause creates an unnamed node, a node with a label, a node with a label and a name and a relationship. Note that, to create a relationship, the nodes need to be matched first. 

<ul>
  <li><code>CREATE (n) RETURN n</code></li>
  <li><code>CREATE (n:Experiment) RETURN n</code></li>
  <li><code>CREATE (n:Experiment {name: "Test"}) RETURN n</code></li>
  <li><code>MATCH (a:Experiment), (b:Specimen) CREATE (a)-[r:PART_OF]-(b) RETURN r</code></li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MERGE</code></b><br>
The <code>MERGE</code> clause matches or creates a node or a relationship. If the specified pattern already exists, it is matched, and if it does not exist, it is created. It is possible to specify nodes with labels and/or properties, so nodes are only created if a node with the exact same label and properties does not yet exist.  
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>DELETE</code></b><br>
The <code>DELETE</code> clause deletes the node or relationship specified after the clause. Nodes that have relationships, cannot be deleted. To delete a node and all its relationships, use <code>DETACH DELETE</code>. For exammple, the query below deletes all nodes and relationships in a database. 

<code>MATCH (n) DETACH DELETE n</code>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>WHERE</code></b><br>
The <code>WHERE</code> clause extends constraints to the patterns previously described after a <code>MATCH</code> or <code>WITH</code> clause. In the example below, the <code>WHERE</code> clause is used to state that the the node in the <code>MATCH</code> clause should have a specific name. <code>WHERE</code> clauses are particularly helpful when used with operators like <code>AND</code>, <code>OR</code>, <code>NOT</code> and <code>IN</code>. They can also be used to filter on properties using the < and > operators. 

<code>MATCH (n) WHERE n.name = 'g__Escherischia' RETURN n</code>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>WITH</code></b><br>
The <code>WITH</code> clause allows queries to be chained together. Often, the <code>WITH</code> clause refers to a pattern matched before the clause and subsets this pattern to be used in the next part of the query. In the example below, the <code>WITH</code> clause is used to select a single node from a query and connect this node to another node. In this case, the clause finds any <code>Taxon</code> node connected to at least two edges and then finds part of its taxonomy. 

<code>MATCH (a:Edge)--(x:Taxon)--(b:Edge) WITH x MATCH p=(x)--(:Family)--(:Order)--(:Class)--(:Phylum)--(:Kingdom) RETURN p</code>
</div>
