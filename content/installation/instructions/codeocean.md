---
title: "Code Ocean"
description: ""
lead: ""
date: 2021-05-11T14:39:07+02:00
lastmod: 2021-05-11T14:39:07+02:00
draft: false
images: []
menu: 
  installation:
    parent: "Installation"
weight: 4
toc: true
---

<a href="https://codeocean.com/capsule/0482418">Access the Code Ocean capsule here.</a><br>

The mako package and the database used to present this package can also be accessed via Code Ocean. If you use mako this way, you will not need to install any of the dependencies; however, the Code Ocean capsule needs to set up the Neo4j database for each use and this can be time-consuming. The capsule is therefore suitable for trying out mako and Neo4j, but less so for running specific analyses. Moreover, it is not possible to run the Neo4j Browser from the capsule. 

Code Ocean is a platform for sharing computational research. Compute capsules include not only scientific software, but also scripts necessary to demonstrate the functionality of this software. The capsules do not need to be installed but are directly executable from the Code Ocean servers. Consequently, the cost of trying out new software is drastically reduced. 

In short, the main <code>run</code> script configures and starts a Neo4j database. The script also uses mako to write all files to this database. Three scripts are then used to generate case study results: the <code>run_query.py</code> Python script, which runs custom queries, the <code>run_motifs.py</code> Python script, which generates data for figures, and the <code>plot_motifs.R</code> R script, which uses this data to generate figures used to present mako's features. 

Since compute capsules shut down at the end, the database is deleted afterwards. Hence, uploading all data sets can take a long time and the <code>run</code> script needs to be adapted slightly to do this; running a database locally or via Docker may be more convenient for running large analyses. However, it is possible to clone the compute capsule and adapt it for your own purposes. If you want to run the Code Ocean scripts on your own machine, follow the <a href="/neo4j/introduction/intro">Neo4j manual</a> to learn how to run up Neo4j locally and check out <a href="https://github.com/ramellose/mako"> mako's Github page</a> for instructions on how to install mako. 

If you run the Code Ocean script to populate a Neo4j database, keep in mind that this can take between 1 and 2 hours. 
