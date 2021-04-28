---
title: "API Overview"
description: ""
lead: ""
date: 2021-04-20T11:36:28+02:00
lastmod: 2021-04-20T11:36:28+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 1
toc: true
---

The API follows an identical structure to the CLI, which has been separated in several modules for ease of use. Importing a class or function from mako therefore can be done as follows:

<ul>    
    <li><code>from mako.scripts.utils import ParentDriver</code></li>
    <li><code>from mako.scripts.base import BaseDriver</code></li>
    <li><code>from mako.scripts.neo4biom import Biom2Neo</code></li>
    <li><code>from mako.scripts.io import IoDriver</code></li>
    <li><code>from mako.scripts.netstats import NetstatsDriver</code></li>
    <li><code>from mako.scripts.metastats import MetastatsDriver</code></li>
    <li><code>from mako.scripts.utils import ParentDriver</code></li>
</ul>

For learning more about the parameters used by a driver, type <code>help(driver)</code>, replacing <code>driver</code> with the name of the driver you are interested in. Note that all classes have private methods which are not explained here. 

All drivers are derived from the ParentDriver class, meaning they share a few parameters that provide information necessary to access the Neo4j database. 

<ul>
  <li><code>filepath</code> File path for reading / writing files and log</li>
  <li><code>encrypted</code> Toggle encryption, for example by setting to False to interact with Docker</li>
  <li><code>user</code> Neo4j username</li>
  <li><code>password</code> Neo4j password</li>
  <li><code>uri</code> Neo4j address</li>
</ul>

For an example of the mako API, please check out <a href="../../demo/query/intro">the querying demo</a>. 

