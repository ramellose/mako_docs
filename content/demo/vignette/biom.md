---
title: "Uploading BIOM file"
description: ""
lead: ""
date: 2021-04-19T11:52:26+02:00
lastmod: 2021-04-19T11:52:26+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 103
toc: true
---

From a terminal, navigate to the location where you downloaded the BIOM file. By storing the config file, we can save ourselves the hassle of typing access information each time. For <code>-fp</code>, fill in the file path where the downloaded BIOM file is stored. 

<code>mako neo4biom -fp . -cf -u neo4j -p test 
-a bolt://localhost:7688 -biom demo.biom </code>

If you access the Neo4j Browser (<a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>) and run the following query, you should be able to access all the nodes connected to taxa:

<code>```MATCH p=(n:Taxon)--() RETURN p LIMIT 50```</code>

<figure>
  <img src="/images/demo_1.PNG" alt="Taxon links to other nodes." width="600"> 
  <figcaption>Figure 1: Taxon links to other nodes.</figcaption>
</figure>

The query <code>MATCH p=(n:Taxon)--() RETURN p LIMIT 50</code> returns 50 patterns consisting of Taxon nodes connected to any other node. For example, many Specimen nodes where the Taxon nodes were found, are returned, as well as the phylogenetic nodes linked to the Taxon nodes (Figure 1). 
