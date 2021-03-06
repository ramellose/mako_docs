---
title: "Uploading networks"
description: ""
lead: ""
date: 2021-04-19T11:49:52+02:00
lastmod: 2021-04-19T11:49:52+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 104
toc: true
---

From a terminal, navigate to the location where you downloaded the network files. Now, only the network files and the file path need to be provided. 

<code>mako io -fp . -cf -net demo_1.graphml demo_2.graphml</code>

If you access the Neo4j Browser (<a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>) and run the following query, you should be able to access all the nodes connected to edges:

<code>```MATCH p=(n:Edge)--() RETURN p LIMIT 50```</code>

<figure>
  <img src="/images/demo_2.PNG" alt="Edge links to taxa and networks." width="600"> 
  <figcaption>Figure 2: Edge links to taxa and networks.</figcaption>
</figure>

The query <code>MATCH p=(n:Edge)--() RETURN p LIMIT 50</code> returns 50 patterns consisting of Edge nodes connected to any other node. Since Edge nodes can connect to Taxon nodes and to Network nodes, these are returned by the query (Figure 2). 

In this case, the shown edges are part of the imported synthetic networks, the <code>demo_1.graphml</code> and the <code>demo_2.graphml</code> files. The interpretation of these networks therefore depends on the type of data that the grapmhl files were based on. If these were association networks, the orange Edge nodes would represent statistically significant links between different OTUs (and therefore do not represent observations of interactions). However, if they were metabolic interaction networks, each Edge node could represent an exchange of metabolites. 