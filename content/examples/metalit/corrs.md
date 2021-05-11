---
title: "Association network"
description: ""
lead: ""
date: 2021-05-06T09:39:25+02:00
lastmod: 2021-05-06T09:39:25+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Validation"
weight: 302
toc: true
---

For the remainder of this case study, we will interact with a running Neo4j database. If you do not have such a database available, please take a look at the <a href="/neo4j/introduction/intro">Neo4j section of this web page</a> to learn how to set up one locally or via Docker. 

To upload our association network, we need to open a terminal and navigate to the folder where we stored the files from the previous section. We can upload all files using the <code>neo4biom</code> and <code>io</code> modules. Remember to adjust the address and password if those are different for your Neo4j instance!

<pre><code>
mako neo4biom -u neo4j -p test -a neo4j://localhost:7688 -cf -biom 11766.biom 
mako io -cf -net 11766.graphml
</pre></code>

In the next part of this case study, we will need to parse a XML file so it can be uploaded to Neo4j. Because this requires some custom scripts, we will use the mako API rather than the CLI to do so. It can therefore be helpful to run the remainder of the case study from a Python IDE. 
