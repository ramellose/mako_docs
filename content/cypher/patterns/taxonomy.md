---
title: "Complex queries"
description: ""
lead: ""
date: 2021-05-07T18:41:34+02:00
lastmod: 2021-05-07T18:41:34+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Patterns"
weight: 203
toc: true
---

The following more complex queries use mako's database schema to carry out more intricate operations that require the use of <code>WHERE</code> and <code>WITH</code> statements. 

<pre><code>
MATCH (n:Family)--(a:Taxon)--(b:Edge)--(c:Network) 
WITH n, count(c) AS num, collect(distinct(c.name)) AS networks
WHERE num > 2
RETURN n.name, networks
</code></pre><br>
This query finds a pattern that links taxonomic families to network. It then collects the family names and all unique network names and filters the pattern so all results occur in at least two networks. 

<pre><code>
MATCH p=(a:Order)--()--(x:Edge)--()--(b:Order), 
q=(a:Order)--()--(y:Edge)--()--(b:Order) 
RETURN p, q</code></pre><br>
<code></code><br>
This query finds two patterns, which both have the same taxonomic orders but distinct edges. Therefore, these edges contain different taxa but have similar taxonomic composition. 

<pre><code>
MATCH p=(a:Order)--()--(x:Edge)--()--(b:Order), 
q=(a:Order)--()--(y:Edge)--()--(b:Order) 
WHERE x.weight > 0 AND y.weight < 0 
RETURN p, q LIMIT 1</code></pre><br>
This query finds the same pattern as bove, but it specifies that one edge should have a positive weight and the other should have a negative weight. 

For additional examples of complex queries, take a look at <a href="/examples/intro">the case studies</a>, where we write queries to answer specific biological questions. 