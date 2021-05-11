---
title: "Simple queries"
description: ""
lead: ""
date: 2021-05-07T17:25:02+02:00
lastmod: 2021-05-07T17:25:02+02:00
draft: False
images: []
menu: 
  cypher:
    parent: "Patterns"
weight: 202
toc: true
---

The following simple queries are able to access microbiome data written to a Neo4j database by mako. 

<code>MATCH (:Genus {name: 'g__Escherichia'})--(:Taxon)--(:Edge)--(n:Taxon) RETURN n</code><br>
This query returns all taxa that have an association with a taxon belonging to the genus <i>Escherichia</i>. 

<code>MATCH p=(a:Edge)--(:Taxon)--(b:Edge) WHERE a.name <> b.name RETURN p</code><br>
This query returns all patterns containing a taxon with two unique edges. 

<code>MATCH p=(:Order {name: 'o__Bacillales'})--(:Taxon)--(b:Edge)--(:Taxon)--(:Order {name: 'o__Clostridiales'}) RETURN p</code><br>
This query returns all pattern containing edges between taxa belonging to Bacillales and Clostridiales. 

<code>MATCH p=(:Taxon)--(a:Edge) WHERE a.weight > 0 RETURN p</code><br>
This query returns all patterns with edges with a weight larger than 0. 

<code>MATCH p=(a:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(a) RETURN p</code><br>
This query returns a 3-node clique, where the first <code>Taxon</code> node is also the last node completing the clique. 
