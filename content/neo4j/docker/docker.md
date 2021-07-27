---
title: "Setting up Docker"
description: ""
lead: ""
date: 2021-04-20T16:24:59+02:00
lastmod: 2021-04-20T16:24:59+02:00
draft: false
images: []
menu: 
  neo4j:
    parent: "Docker"
weight: 102
toc: true
---

<a href="https://www.docker.com/why-docker">Docker</a> is a convenient tool for virtualization. Docker containers contain a standardized environment that can be run from any desktop or via the cloud, solving many issues with compatibility across operating systems. By running software via Docker instead of directly on a desktop, it becomes possible to run different versions of dependencies side-by-side without affecting existing installations. As a result, running Neo4j via Docker can be more convenient. 

Mac and Windows users need to use <a href="https://www.docker.com/get-started">Docker Desktop</a>, while Linux users can run Docker containers after <a href="https://docs.docker.com/engine/install/ubuntu/">installing docker-engine</a>. 
Please make sure Docker can run on your machine using one of the above links. Mac and Windows users also need to launch Docker Desktop after installation to start using Docker containers.

After installing Docker (Desktop), the Neo4j Docker container can be setup by running the commands below from a terminal. Each time you call the Docker container for Neo4j, a Neo4j Docker image is pulled from DockerHub and used to start a container. You can specify a range of commands to configure the Neo4j Docker image. For an expansive guide, please take a look at <a href="https://neo4j.com/developer/docker-run-neo4j/">the Neo4j Docker how-to</a>. 

<pre><code>
docker run --rm \
-d \
--publish=7475:7474 --publish=7688:7687 \
--name=neo4j \
--env NEO4J_AUTH=neo4j/test \
neo4j:latest
</pre></code>

The <code>--rm</code> flag tells Docker to clean up after exiting, while the <code>-d</code> flag means the Docker can be accessed separately. 

Importantly, the <code>--publish</code> flag changes exposed ports, so the Neo4j container can be accessed via navigating to <a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a> in a browser and setting the connection to <code>neo4j://localhost:7688</code> or <code>bolt://localhost:7688</code>. The <code>--name</code> flag sets the container's name, the <code>--env</code> flag sets the username and password for the Neo4j container and <code>neo4j:latest</code> tells Docker to pull the latest image. To stop the Docker container is then quite straightforward:

<code>
docker stop neo4j
</code>
<br>
<br>
To start using the Neo4j Docker container, simply run the first command or a modified version of this command, and then navigate to Neo4j Browser to access the database. By passing these parameters to mako, you can have mako import BIOM files and networks to the database. Keep in mind that by default, the data folder is cleared once the container is shut down, so Docker is not as useful for maintaining a local database. 
