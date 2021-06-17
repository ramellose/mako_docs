---
title: "Neo4j Browser"
description: ""
lead: ""
date: 2021-04-20T16:26:06+02:00
lastmod: 2021-04-20T16:26:06+02:00
draft: false
images: []
menu: 
  neo4j:
    parent: "Browser"
weight: 401
toc: true
---

Neo4j Browser is a user interface for Neo4j that can be accessed via a browser. When a Neo4j service or console application is running locally, the Neo4j Browser can be started by navigating to , if port settings are adjusted). Neo4j Browser provides a place to enter Cypher queries and visualize simple results. You can find more details on Neo4 Browser on the <a href="https://neo4j.com/developer/neo4j-browser/">Neo4j Browser section of the developer guides</a>. 

To use Neo4j Browser, please follow the instructions below:
<ul>
  <li>If using <a href="/./local/intro/">default settings</a>:</li>
  <li><ol>
      <li>Navigate to <a href="http://localhost:7474">http://localhost:7474</a> to reach the Neo4j Browser</li>
      <li>Default URL: localhost:7687</li>  
      <li>Default username: neo4j</li>
      <li>Default password: neo4j</li>
  </ol></li>
  <li>If using the <a href="/./docker/docker/">the Docker configuration</a>:</li>
    <li><ol>
      <li>Navigate to <a href="http://localhost:7475">http://localhost:7475</a> to reach the Neo4j Browser</li>
      <li>Default URL: localhost:7688</li>  
      <li>Default username: neo4j</li>
      <li>Default password: test</li>
  </ol></li>
  <li>Click the Connect button to reach the database</li>
  <li>Type queries into the bar above and press the blue triangle to run them</li>
</ul>

<figure>
  <img src="/images/connect.PNG" alt="Interface of Neo4j Browser with bolt://localhost:7688 as connecting URL and username / password authentication." width="600"> 
  <figcaption>Figure 1: Interface of Neo4j Browser with bolt://localhost:7688 as connecting URL and username / password authentication.</figcaption>
</figure>

When you are developing your own Cypher queries, Neo4j Browser is a great tool for testing those queries. Not only will the Browser report which parts of queries are incorrect, there are also a range of other queries that can be used to visualize database structure and query cost. To get a query profile, simply preface your query with <code>PROFILE</code>. 

For more information on how to explore your database, these tutorials may be of interest:
<ul>
  <li><a href="https://neo4j.com/blog/tuning-cypher-queries/">Tuning Cypher</a></li>
  <li><a href="https://neo4j.com/docs/cypher-manual/current/query-tuning/basic-example/">Basic query tuning</a></li>
  <li><a href="https://neo4j.com/blog/data-profiling-holistic-view-neo4j/">Data profiling</a></li>
</ul>
