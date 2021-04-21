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
weight: 8
toc: true
---

Instead of working with the Neo4j database directly, it is also possible to export a specific network to a graphml file or to a running Cytoscape instance with the commands below. Specify the target network with the <code>-net</code> flag. The new network is exported to the specified file path in <code>-fp</code>. The <code>-cyto</code> flag is used to tell mako to export the network to Cytoscape as well. 

{{< alert icon="👉" text="To export a network to Cytoscape, make sure Cytoscape is running first!" >}}


<code>mako io -fp local_filepath -cf -net Genus_demo_1 -cyto -w</code>

<figure>
  <img src="/images/demo_6.PNG" alt="Cytoscape with a network imported from Neo4j." width="600"> 
  <figcaption>Figure 6: Cytoscape with a network imported from Neo4j.</figcaption>
</figure>
