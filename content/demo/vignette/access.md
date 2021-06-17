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
Please check out <a  href="/../neo4j/introduction/intro/">the instructions on how to start a Neo4j database</a>, if you do not have one available yet. There needs to be an online database for mako to access before any of the following commands will work. The software will connect to the running database and interact with this. 

For this tutorial, it is assumed that the settings to connect to Neo4j are identical to those used for the Docker instance. Consequently, the Bolt address is <code>bolt://localhost:7688</code>. If you are using the default address, make sure to use <code>bolt://localhost:7687</code> in your commands. 

You can follow exactly what mako is doing via the Neo4j Browser. Please find a detailed guide to the Browser here: <a href="https://neo4j.com/developer/neo4j-browser/">Neo4j Browser guide</a>. If you are running Neo4j locally, you can access the Neo4j Browser via <a href="http://localhost:7475/browser">http://localhost:7475/browser</a> (Docker setup) or via <a href="http://localhost:7474/browser">http://localhost:7474/browser</a> (default setup). 