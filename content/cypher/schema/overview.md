---
title: "Overview"
description: ""
lead: ""
date: 2021-04-21T16:29:49+02:00
lastmod: 2021-04-21T16:29:49+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Schema"
weight: 2
toc: true
---

The database schema used by mako was designed to meet several demands:
<ul>
    <li>Simple querying of BIOM data</li>
    <li>Simple querying of network data</li>
    <li>Respect hierarchical structure of taxonomic tree</li>
    <li>Straightforward access of networks for meta-analyses</li>
    <li>Flexible inclusion of metadata</li>
</ul>

As a result, each of the items always present in networks and BIOM files have their own node label and can more easily be accessed. In contrast, property nodes are more flexible and can be connected to any other node. The complete schema, sufficient to import BIOM files and network files, therefore specifies both standard node types and node relationships (Figure 1). 

<figure>
  <img src="/images/schema_micro.pdf" alt="Schema for storing BIOM files and microbial networks." width="600"> 
  <figcaption>Figure 1: Schema for storing BIOM files and microbial networks.</figcaption>
</figure>
