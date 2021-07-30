---
title: "Set up database"
description: ""
lead: ""
date: 2021-04-19T11:52:52+02:00
lastmod: 2021-04-19T11:52:52+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 102
toc: true
---

{{< alert icon="👉" text="The rest of this vignette assumes that you have a running instance of Neo4j to work with." >}}
<br>
Please check out <a  href="https://ramellose.github.io/mako_docs/neo4j/introduction/intro/">the instructions on how to start a Neo4j database</a>, if you do not have one available yet. There needs to be an online database for mako to access before any of the following commands will work. The software will connect to the running database and interact with this. 

For this tutorial, it is assumed that the settings to connect to Neo4j are identical to those used for the Docker instance. Consequently, the Bolt address is <code>bolt://localhost:7688</code>. If you are using the default address, make sure to use <code>bolt://localhost:7687</code> in your commands. 

{{< alert icon="👉" text="Connect to the Neo4j Browser to follow along with the demo." >}}

Y<br>ou can follow exactly what mako is doing via the Neo4j Browser. For complete instructions on accessing the Neo4j Browser, please continue to <a href="../../../neo4j/browser/browser">the Neo4j Browser page</a>.  