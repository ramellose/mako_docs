---
title: "Standardized queries"
description: ""
lead: ""
date: 2021-05-07T17:40:38+02:00
lastmod: 2021-05-07T17:40:38+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Patterns"
weight: 1
toc: true
---

We can use <a href="../../schema/intro">the schema specified below</a> to design sets of standard queries that can be reused across microbiome studies. Because we have a number of standard node labels that should only have connections with certain other node labels, we can omit information from our queries that we would otherwise need to specify. 

For example, we know that a <code>Family</code> node is never directly connected to an <code>Edge</code> node, but must always pass through a <code>Taxon</code> node. There is no other node that is able to connect taxonomy nodes to edges. As a result, both queries below should always give the same results: 

<code>MATCH (:Family {name: "f__Rhodobacteraceae"})--(:Taxon)--(:Edge)--(:Taxon)--(b:Family) RETURN b</code><br>
<code>MATCH (:Family {name: "f__Rhodobacteraceae"})--()--(:Edge)--()--(b:Family) RETURN b</code>

However, we should specify the <code>Edge</code> node; according to the database schema, the pattern would otherwise also match all families that are found in the same specimen, since the central node in the pattern could also be a <code>Specimen</code> node. 

In this section, we will go through several increasingly complex queries that can be useful when with mako. Since mako writes all files to the Neo4j database in the same way, the same queries can be reused for most data sets. 