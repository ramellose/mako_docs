---
title: "Constructing intersection"
description: ""
lead: ""
date: 2021-04-19T11:49:36+02:00
lastmod: 2021-04-19T11:49:36+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 105
toc: true
---

The command below generates a network containing all matching edges between <code>demo_1</code> and <code>demo_2</code>. By using the <code>-w</code> flag, mako is told to ignore whether edges have matching edge weights or not. The command below omits this, so edges are only considered part of an intersection if they have the same edge weight. 

<code>mako netstats -fp local_filepath -cf</code>


If you access the Neo4j Browser (<a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>) and run the following query, you should be able to access all the edges part of sets:

<code>```MATCH p=(n:Set)--() RETURN p LIMIT 50```</code>


<figure>
  <img src="/images/demo_3.PNG" alt="Network sets with edges." width="600"> 
  <figcaption>Figure 3: Network sets with edges.</figcaption>
</figure>

