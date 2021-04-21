---
title: "Merge network by taxonomy"
description: ""
lead: ""
date: 2021-04-19T11:49:07+02:00
lastmod: 2021-04-19T11:49:07+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 7
toc: true
---

The command below merges networks by taxonomic level. For example, by merging to genus, both nodes assigned to <i>Escherichia</i> are merged into a single node, and by merging to order, the Halaerobiales nodes are merged as well. All lower taxonomic levels are also merged by running this command. Simply specify the taxonomic level after the <code>agglom</code> command. 

<code>mako metastats -fp local_filepath -cf -agglom order</code>

If you access the Neo4j Browser (<a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>) and run the following query, you should be able to access two of the agglommerated networks:

<code>MATCH p=(n:Network {name: 'Genus_demo_1'})--(:Property) RETURN p LIMIT 50</code>

<code>MATCH p=(n:Network {name: 'Order_demo_1'})--(:Property) RETURN p LIMIT 50</code>

<figure>
  <img src="/images/demo_5.PNG" alt="Network merged by taxonomy." width="600"> 
  <figcaption>Figure 5: Network merged by taxonomy.</figcaption>
</figure>

