---
title: "mako netstats"
description: ""
lead: ""
date: 2021-04-20T11:33:52+02:00
lastmod: 2021-04-20T11:33:52+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 6
toc: true
---
The <code>netstats</code> module can be used to carry out set operations on networks in the Neo4j database, leading to creation of Set nodes that contain the intersections, unions or differences across (groups of) networks. If no networks are specified, operations are carried out across all networks. 

By default, intersections only include edges with identical weights; so for an edge to be detected as present in 3 networks, it needs to have the same weight across all 3 networks. For the difference, if edges have different weights, they are considered unique edges so two edges with the same partners may be part of the difference. If the <code>-w</code> flag is used, this behaviour is reversed. 

The fractions specified after <code>-frac</code> define partial intersections, e.g. all edges present in half of all networks. 

<ul>
  <li><code>-net</code> One or more Network names, by default all networks</li>
  <li><code>-w</code> If flagged, edge weights are not taken into account</li>
  <li><code>-frac</code> One or more fractions that are used to define subgroups for intersections</li>
</ul>