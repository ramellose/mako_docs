---
title: "Connect to Neo4j"
description: ""
lead: ""
date: 2021-04-21T09:54:25+02:00
lastmod: 2021-04-21T09:54:25+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Pisaster"
weight: 4
toc: true
---

We can use the <a href="https://neo4j.com/developer/docker-run-neo4j/">Neo4j Docker</a> container to run Neo4j without needing to deal with a complicated setup. 
For this demo, the following command can be run from a terminal to start the Docker container: 

<pre><code>
docker run --rm \
-d \
--publish=7475:7474 --publish=7688:7687 \
--name=neo4j \
--env NEO4J_AUTH=neo4j/test \
neo4j:latest
</code></pre>

We can navigate to the Neo4j Browser via the specified port: <a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>. To connect to Neo4j, we then fill in the rest of the information specified in the command; note that NEO4J_AUTH contains the username and password for the Neo4j database in the Docker container (Fig 3). Do not forget to change the port settings in the browser window, the neo4j or bolt connection needs to be set to 7688 rather than the default 7687. 

<figure>
  <img src="/images/connect.PNG" alt="Interface of Neo4j Browser with bolt://localhost:7688 as connecting URL and username / password authentication." width="600"> 
  <figcaption>Figure 3: Interface of Neo4j Browser with bolt://localhost:7688 as connecting URL and username / password authentication.</figcaption>
</figure>

