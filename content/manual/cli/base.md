---
title: "mako base"
description: ""
lead: ""
date: 2021-04-20T11:33:29+02:00
lastmod: 2021-04-20T11:33:29+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 3
toc: true
---

The <code>base</code> module can start a Neo4j Desktop if no Neo4j Desktop process has been started already, or safely shut down Neo4j Desktop if the process has been stored and the process ID is available in the config file. Additionally, the module can clear the database or check constraints.

If connecting to a Docker instance or other running instance of Neo4j, only the <code>-clear</code> and <code>-check</code> functions of the <code>base</code> module are relevant. 

<ul>
  <li><code>-n</code> Filepath to neo4j folder (only relevant for running Neo4j desktop)</li>
  <li><code>-start</code> Start Neo4j Desktop. Flag <code>-cf</code> to store process ID</li>
  <li><code>-clear</code> Clears running Neo4j database</li>
  <li><code>-quit</code> Uses stored process ID in config to safely shut down Neo4j desktop</li>
  <li><code>-check</code> Checks if relationships in the database violate database schema constraints</li>
</ul>


