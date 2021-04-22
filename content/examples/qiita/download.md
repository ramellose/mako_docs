---
title: "Download"
description: ""
lead: ""
date: 2021-04-21T16:31:02+02:00
lastmod: 2021-04-21T16:31:02+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Qiita"
weight: 2
toc: true
---

First, download the mako.dump file from <a href="https://github.com/ramellose/mako/releases">the mako releases page</a>. This file was created by uploading 60 BIOM files and network files to the Neo4j database and then using neo4j-admin to create a dump file. Such a file is much faster to restore a complete database. Save the file to a folder named <b>data</b>, then navigate to the folder containing the data folder on your command line. See the screenshot below for an example data folder in Ubuntu. 

<figure>
  <img src="/images/filepath.PNG" alt="Screenshot with mako.dump file location." width="600"> 
  <figcaption>Figure 1: Screenshot with mako.dump file location.</figcaption>
</figure>

