---
title: "Paine's food web"
description: ""
lead: ""
date: 2021-04-21T09:53:41+02:00
lastmod: 2021-04-21T09:53:41+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Pisaster"
weight: 1
toc: true
---

<a href="https://neo4j.com/">Neo4j</a> is a native graph database, meaning it can store biological data in a way that is more intuitive to people unfamiliar with SQL. In this guide, we will use Paine's food web (Paine, 1966) to demonstrate how database schemas work and how you can use Cypher queries to access a Neo4j database. We will use the <a href="https://neo4j.com/developer/neo4j-browser/">Neo4j Browser</a> to visualize query outcomes. All code in this guide will be in pure Cypher, meaning you can run it from the browser interface.

The Cypher queries in this file can be used to recreate Paine's network in your own Neo4j database. If you want to know how to run Neo4j locally, connect to a server or connect to the Docker container provided with this guide, we refer to the instructions described in: <a href="http://localhost:1313/neo4j/docker/docker/">Setting up Docker</a>. 

Paine, R. T. (1966). Food web complexity and species diversity. <i>The American Naturalist, 100</i>(910), 65-75.