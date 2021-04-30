---
title: "Code Ocean"
description: ""
lead: ""
date: 2021-04-29T13:51:57+02:00
lastmod: 2021-04-29T13:51:57+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Qiita"
weight: 4
toc: true
---

The entire curated database is also availabe through Code Ocean via the <a href="https://codeocean.com/capsule/0482418">mako compute capsule</a>. 
Code Ocean is a platform for sharing computational research. Compute capsules include not only scientific software, but also scripts necessary to demonstrate the functionality of this software. The capsules do not need to be installed but are directly executable from the Code Ocean servers. Consequently, the cost of trying out new software is drastically reduced. 

In short, the main <code>run</code> script configures and starts a Neo4j database. The script also uses mako to write all files to this database. Three scripts are then used to generate case study results: the <code>run_query.py</code> Python script, which runs custom queries, the <code>run_motifs.py</code> Python script, which generates data for figures, and the <code>plot_motifs.R</code> R script, which uses this data to generate figures used to present mako's features. 

Since compute capsules shut down at the end, the database is deleted afterwards. Hence, uploading all data sets can take a long time and the <code>run</code> script needs to be adapted slightly to do this; running a database locally or via Docker may be more convenient for running large analyses. However, it is possible to clone the compute capsule and adapt it for your own purposes. 

In the <a href="../../motifs/intro">Motifs tutorial</a> and the <a href="../../propionate/intro">Propionate tutorial</a>, we will explain the <code>run_motifs.py</code> in more detail to illustrate how mako and its database schema is used to access biologically informative patterns. 