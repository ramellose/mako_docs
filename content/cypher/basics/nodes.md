---
title: "Nodes and relationships"
description: ""
lead: ""
date: 2021-05-07T17:23:09+02:00
lastmod: 2021-05-07T17:23:09+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Basics"
weight: 3
toc: true
---

Cypher queries include patterns that describe nodes and relationships. The syntax specifies whether a part of a query is a node or a relationship. 

Specifically, in the query below, <code>n</code> and <code>m</code> are nodes, surrounded by <code>()</code>. The relationship is represented by <code>--</code>. Values like <code>m</code> and <code>n</code> are parameters, which can be passed to later clauses. 

<code>MATCH p=(n)--(m) RETURN p</code>


To add details to the relationship, brackets <code>[]</code> should be added. To specify the direction of a relationship, arrowheads > or < can also be included. In this case, the query finds a node 
<code>n</code> that is part of <code>m</code>. 

<code>MATCH p=(n)-[x]->(m) RETURN p</code>

Nodes have labels and relationships have types. These are indicated after <code>:</code> and can be preceded by a parameter, but this is not necessary if whole patterns including the node or relationship are returned, rather than specific nodes or relationships. Node labels especially can make it much faster to run Cypher queries, since they drastically reduce the number of nodes that needs to be matched to the pattern. 

Note that the Cypher style guide recommends writing relationship types in upper-case with an underscore between words, as is shown below. 

<code>MATCH (n:Specimen)-[x:PART_OF]->(m:Experiment) RETURN x</code><br>
<code>MATCH p=(:Specimen)-[:PART_OF]->(:Experiment) RETURN p</code>

In addition to labels and types, nodes and relationships can have properties. The syntax for accessing properties is identical across nodes and relationships. The queries below find an experiment linked a sample with a pH of 8 and a taxon with a Spearman correlation of 0.6 that is linked to a pH node. 

<code>MATCH (n:Specimen {name: "Sample 1", pH: 8})-[x:PART_OF]->(m:Experiment) RETURN m</code><br>
<code>MATCH (n:Taxon)-[x:SPEARMAN_CORRELATION {value: 0.6}]->(:Property {name: "pH"}) RETURN n</code>

Properties can be specified in multiple ways: one is to include them inside the node or relationship in <code>{}</code> brackets, as shown above. The other is to specify the node or relationship as a parameter and refer to the property after it. The latter is shown below; this query finds any taxa with a positive Spearman correlation to pH.

<code>MATCH (n:Taxon)-[x:SPEARMAN_CORRELATION]->(:Property {name: "pH"}) WHERE x.value > 0 RETURN n</code>
