---
title: "CLI Overview"
description: ""
lead: ""
date: 2021-04-20T11:52:09+02:00
lastmod: 2021-04-20T11:52:09+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 102
toc: true
---

The CLI has been separated in several modules for ease of use. Selecting a module is done by including the module name in the script call, like so:

<ul>
    <li><code>mako base</code></li>
    <li><code>mako neo4biom</code></li>
    <li><code>mako io</code></li>
    <li><code>mako netstats</code></li>
    <li><code>mako metastats</code></li>
    <li><code>mako manta</code></li>
    <li><code>mako anuran</code></li>
</ul>

For learning more about the parameters used by each module, type <code>mako module -h</code> in your terminal, replacing <code>module</code> with the name of the module you are interested in. In the next sections, a brief overview of module functionalities is provided. 

Several parameters are present across all modules. These provide information necessary to access the Neo4j database. By setting the <code>-cf</code> flag, Neo4j access information only needs to be stored once as mako will generate a config file that can be accessed. This is <b>not</b> a protected file, so this should not be used when addressing highly secured databases. However, for local Neo4j Desktop and Docker instances, the config file saves repeated entry of details. 

<ul>
  <li><code>-fp</code> File path for reading / writing files and log</li>
  <li><code>-cf</code> Use flag to store Neo4j access information</li>
  <li><code>-u</code> Neo4j username</li>
  <li><code>-p</code> Neo4j password</li>
  <li><code>-a</code> Neo4j address</li>
</ul>
