---
title: "Export to Cytoscape"
description: ""
lead: ""
date: 2021-04-19T11:48:54+02:00
lastmod: 2021-04-19T11:48:54+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 108
toc: true
---

Instead of working with the Neo4j database directly, it is also possible to export a specific network to a graphml file or to a running Cytoscape instance with the commands below. Cytoscape is an open source platform for visualizing networks; if you have not yet installed it, download it from the <a href="https://cytoscape.org/"> Cytoscape homepage</a>. Specify the target network with the <code>-net</code> flag. The new network is exported to the specified file path in <code>-fp</code>. The <code>-cyto</code> flag is used to tell mako to export the network to Cytoscape as well. 

{{< alert icon="👉" text="To export a network to Cytoscape, make sure Cytoscape is running first!" >}}


<code>mako io -fp . -cf -net Genus_demo_1 -cyto -w</code>

<figure>
  <img src="/images/demo_6.PNG" alt="Cytoscape with a network imported from Neo4j." width="600"> 
  <figcaption>Figure 6: Cytoscape with a network imported from Neo4j.</figcaption>
</figure>

The Genus_demo_1 wnetwork as previously generated using the mako module; by specifying this network name, it is possible to export the network to Cytoscape. When doing so, mako converts the Neo4j representation of the network to a conventional network representation where edges are only relationships between nodes (Figure 6). 

{{< alert icon="👉" text="To clear the database for future use, run the query MATCH (n) DETACH DELETE n." >}}
