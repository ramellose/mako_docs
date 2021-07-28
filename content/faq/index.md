---
title: "FAQ"
description: ""
date: 2021-07-28T14:01:51+02:00
lastmod: 2021-07-28T14:01:51+02:00
draft: false
images: []
---

If you run into a problem with any of the demos or case studies, feel free to open an issue here: <a href="https://github.com/ramellose/mako_docs/issues">https://github.com/ramellose/mako_docs/issues</a>. 

If your problem is related to mako itself, you can open an issue at the mako Github page: <a href="https://github.com/ramellose/mako/issues">https://github.com/ramellose/mako/issues</a>.

##### After installing via conda, the <code>mako -h</code> command does not work
Please check if you installed mako from the correct source. During installation, the mako source should look similar to the image below. 
<figure>
  <img src="/images/conda_source.png" alt="Screenshot of the command line environment showing the source for mako installation." width="600"> 
  <figcaption>Screenshot of the command line environment showing the source for mako installation.</figcaption>
</figure>

##### I cannot find the username and password credentials for the Neo4j Browser
Please check <a href="../neo4j/browser/browser">the Neo4j Browser page</a> for configurations used in the case studies presented on this website. If you are running Neo4j from Docker, the username and password are set using the NEO4J_AUTH part of the Docker command. 

##### The mako software raises a WebSocket Connection Failure error
If you experience this error, you are likely using the wrong parameters for connecting to the Neo4j database. Please check <a href="../neo4j/browser/browser">the Neo4j Browser page</a> for an overview of alternative configurations of the database and supply the appropriate connection parameters to the mako software.

##### Neo4j Browser states that database access is not available 
Like the error above, you are likely using the wrong parameters for connecting to the Neo4j database. Please check <a href="../neo4j/browser/browser">the Neo4j Browser page</a> for an overview of alternative configurations of the database.

##### The mako software cannot import files
Please check if this is due to a path error. If you are running mako outside the directory where your files are stored, you need to give a filepath with the <code>-fp</code> parameter. If you navigate to the directory where your files are, you can omit this parameter. Note that you either need to give a folder name or file names. You need to unzip zipped files into a folder before mako can use them. 

