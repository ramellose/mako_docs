---
title: "Introduction"
description: ""
lead: ""
date: 2021-04-21T16:30:54+02:00
lastmod: 2021-04-21T16:30:54+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Qiita"
weight: 1
toc: true
---

For presenting mako, we constructed a curated database of 60 data sets and 60 networks which were collected from Qiita (Gonzalez et al., 2018). 
We can load a dump of mako's 60-network database into a Docker container or a local Neo4j database. The following commands carry out such a task. Keep in mind that you need to use a Neo4j version equal to the version that the database was created in, in this case 4.2.0. With the Docker command, you will automatically download and start the correct version. Otherwise, you can select the button in the left bottom corner of the Neo4j Browser to see which version you are running. 

For common issues with setting up the Docker, please check out the Troubleshooting section at the end.

When you change Neo4j versions, the browser cache may cause you to load an older version of the Neo4j Browser. Make sure to clear your cache in between switching versions. The exact steps for clearing your browser cache vary per browser. 

<a href="https://www.nature.com/articles/s41592-018-0141-9">Gonzalez, A., Navas-Molina, J. A., Kosciolek, T., McDonald, D., Vázquez-Baeza, Y., Ackermann, G., ... & Knight, R. (2018). Qiita: rapid, web-enabled microbiome meta-analysis. <i>Nature methods, 15</i>(10), 796-798.</a>