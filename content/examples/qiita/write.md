---
title: "Write to database"
description: ""
lead: ""
date: 2021-04-21T16:31:20+02:00
lastmod: 2021-04-21T16:31:20+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Qiita"
weight: 3
toc: true
---

The dump file can be written both to a local Neo4j database, and to a Docker file. The former is a bit simpler, but requires you to download the exact Neo4j version used to generate the dump file, 

<h5>Writing the dump file to a local Neo4j database</h5>
If you have a running local instance of Neo4j, you can simply use the command below from the neo4j folder. Make sure to adapt the --from file path to the file path where you have saved the mako.dump file.
<br><br>
<code>
bin/neo4j-admin load --from=/data/mako.dump --database=neo4j --force
exit 
</code>

<h5>Uploading dump file to a Docker container</h5>
To upload the database, a Docker container needs to be initialized and bound to a local volume. This requires some extra steps to mount the volume and save the dump file there. 
 When you call the Neo4j Docker, do not forget to specify the version name; specifying the wrong version may lead to the database loading incorrectly. 

If you still have a Docker container with the same name running, stop this container first:

<code>
docker stop neo4j
</code>
<br><br>

Otherwise, use the command below to mount a folder named data and shut down the container after starting it. Make sure the data path matches the path to your dump file, so navigate to this location if applicable!

For Windows:<br>
<pre><code>
docker run -d -v 
           ./data:/data 
           --publish=7475:7474 
           --publish=7688:7687 
           --name=neo4j 
           --env NEO4J_AUTH=neo4j/test 
           neo4j:4.2.0
</code></pre>

For Unix:<br>
<pre><code>
docker run -d -v 
           data:/data 
           --publish=7475:7474 
           --publish=7688:7687 
           --name=neo4j 
           --env NEO4J_AUTH=neo4j/test 
           neo4j:4.2.0
</code></pre>

Shut down the container:
<pre><code>
docker stop neo4j
</code></pre>

Next, the mako.dump file is copied from the data folder to Neo4j container. This may give a warning about permissions and the folder not being writable, but the warning should not affect the Docker container. 

For Windows:<br>
<code>
docker cp ./data/mako.dump neo4j:/data/mako.dump
</code>

For Unix:<br>
<code>
docker cp data/mako.dump neo4j:/data/mako.dump
</code>

Then we restart the Neo4j docker, but append the script so that a bash shell is opened. 

For Windows:
<pre><code>
docker run -i -v 
           ./data:/data 
           --publish=7475:7474 
           --publish=7688:7687
           -t neo4j 
           /bin/bash
</code></pre>

For Unix:
<pre><code>
docker run -i -v 
           data:/data 
           --publish=7475:7474 
           --publish=7688:7687 
           -t neo4j 
           /bin/bash
</code></pre>

From the bash shell, we call the neo4j-admin script and use it to restore the neo4j database from the mako.dump file. 

<code>
bin/neo4j-admin load --from=/data/mako.dump --database=neo4j --force
</code>
<br><br>
To measure the amount of time it takes to run the script, you can also call the below command instead. <br><br>
<code>
%SECONDS=0 ; bin/neo4j-admin load --from=/data/mako.dump --database=neo4j --force ; echo $SECONDS
</code>
<br><br>
Finally, we can restart the Docker container. Give it a minute or two to restore the database; afterwards, you should be able to interact with it via the Neo4j Browser at <a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>. Make sure to fill in the correct credentials when you log in to the database. 
<br><br>
<code>
docker start neo4j
</code>
<br><br>
To remove the container, use the following command:
<br><br>
<code>
docker container rm neo4j
</code>
<br><br>
In a Unix environment, the complete sequence to start the database should look something like below:

<figure>
  <img src="/images/commands_ubuntu.PNG" alt="Screenshot of commands to restore mako dump." width="600"> 
  <figcaption>Figure 2: Screenshot of commands to restore mako dump.</figcaption>
</figure>