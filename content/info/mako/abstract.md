---
title: "Abstract"
description: ""
date: 2021-04-19T10:58:02+02:00
lastmod: 2021-04-19T10:58:02+02:00
draft: false
menu:
  info:
    parent: "mako"
images: []
---

While meta-analytical approaches are increasingly adopted in a range of studies, no framework exists that facilitates flexible and intuitive methods of storage and analysis for microbial association networks. Static network databases are unsuitable for such networks as microbial network construction tools evolve rapidly and do not usually lead to generation of validated microbial interaction networks. Consequently, the analysis of microbial associations demand a more flexible setup that can integrate a wealth of data. To achieve this, we developed mako, a software package for the rapid and simple construction and use of network databases from microbiome data. 

Mako provides an interface between standard microbiome formats and Neo4j graph databases via a database schema based on semantic web ontologies. It can rapidly populate such databases from BIOM files, tab-delimited files, network files and edge lists of custom properties through its use of batched Cypher queries. Moreover, mako uses HTTP requests to export networks (or derived database items) to Cytoscape, supporting visualization of smaller subsets of the database. 

This web page includes all documentation and case studies describing mako, as well as detailed information on how to set up your own Neo4j databases. Find the latest updates on <a href="https://github.com/ramellose/mako">the Github page</a>. 