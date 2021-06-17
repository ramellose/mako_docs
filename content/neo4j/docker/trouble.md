---
title: "Troubleshooting"
description: ""
lead: ""
date: 2021-04-21T16:31:25+02:00
lastmod: 2021-04-21T16:31:25+02:00
draft: false
images: []
menu: 
  neo4j:
    parent: "Docker"
weight: 103
toc: true
---

It is possible that you run into issues with the Neo4j configuration. 
For example, the Neo4j Browser may produce an error that the database is unavailable. To print your Docker logs, run Docker without the <code>--rm</code> flag and please run the following command:

<code>
docker logs neo4j
</code>
<br><br>
The logs may suggest that you adjust a parameter in the configuration file. It is not possible to do this within the Docker, but you can adjust the command you use to start the Docker to set these parameters. For detailed instructions, check the <a href="https://neo4j.com/docs/operations-manual/current/docker/configuration/#docker-neo4j-configuration"Neo4j Docker manual</a> and <a href="https://neo4j.com/docs/operations-manual/current/reference/configuration-settings/#configuration-settings">the summary of configuration settings</a>. In brief, you can add any of the configuration settings by adding a NEO4J prefix, replacing . with _ (a single underscore) and replacing _ with __ (double underscores). For example, to allow the database to upgrade, you could run the following command:

<pre><code>
docker run -d -v 
           data:/data 
           --publish=7475:7474 
           --publish=7688:7687
           --name=neo4j 
           --env NEO4J_AUTH=neo4j/test 
           --env NEO4J_dbms_allow__upgrade=true
           neo4j:4.2.0
</pre></code>
