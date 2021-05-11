---
title: "NetstatsDriver"
description: ""
lead: ""
date: 2021-04-28T16:35:58+02:00
lastmod: 2021-04-28T16:35:58+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 207
toc: true
---

This driver extracts nodes and edges from the database that are required for the operations defined in the netstats module.

<div style="outline:0.01em solid black; padding:10px;">
<b><code>NetstatsDriver.graph_union(networks=None)</code></b>

Returns a subgraph (edge list with source, target, network and weight) that contains all nodes present in all networks.
If network names are specified as a list, all nodes present in these two networks are returned.
  
<ul>
  <li><b>networks:</b> List of network names</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>NetstatsDriver.graph_intersection(networks=None, weight=True, fraction=None)</code></b>

Returns a subgraph (edge list with source, target, network and weight) that contains all nodes present in both specified networks.
If no networks are specified, the function returns only nodes that are 
connected to all networks.

<ul>
  <li><b>networks:</b> List of network names</li>
  <li><b>weight:</b> If false, the intersection includes edges with matching partners but different weights</li>
  <li><b>fraction:</b> If specified, fraction of networks that the intersecting node should be in</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>NetstatsDriver.graph_difference(networks=None, weight=True)</code></b>

Returns a subgraph (edge list with source, target, network and weight) that contains all nodes only present in one of the selected networks. If no networks are specified, returns all edges that are unique across multiple networks.

<ul>
  <li><b>networks:</b> List of network names</li>
  <li><b>weight:</b> If false, the intersection includes edges with matching partners but different weights</li>
</ul>
</div>
<br>
