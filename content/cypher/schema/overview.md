---
title: "Database schema for mako"
description: ""
lead: ""
date: 2021-04-21T16:29:49+02:00
lastmod: 2021-04-21T16:29:49+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Schema"
weight: 2
toc: true
---

The database schema used by mako was designed to meet several demands:
<ul>
    <li>Simple querying of BIOM data</li>
    <li>Simple querying of network data</li>
    <li>Respect hierarchical structure of taxonomic tree</li>
    <li>Straightforward access of networks for meta-analyses</li>
    <li>Flexible inclusion of metadata</li>
</ul>

As a result, each of the items always present in networks and BIOM files have their own node label and can more easily be accessed. In contrast, property nodes are more flexible and can be connected to any other node. The complete schema, sufficient to import BIOM files and network files, therefore specifies both standard node types and node relationships (Figure 1). 

<div id="mynetwork", style="height:500px"></div>

<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<script>
  // create an array with nodes
  var nodes = new vis.DataSet([
    { id: 1, label: "Edge", title: 'NCIT:C75923'},
    { id: 2, label: "Experiment", title: 'NCIT:C42790'},
    { id: 3, label: "Network", title: 'NCIT:C61377'},
    { id: 4, label: "Property", title: 'NCIT:C20189'},
    { id: 5, label: "Specimen", title: 'NCIT:C19157'},
    { id: 6, label: "Taxon", title: 'NCIT:C40098'},
    { id: 7, label: "Species", title: 'NCIT:C45293'},
    { id: 8, label: "Genus", title: 'NCIT:C45292'},
    { id: 9, label: "Family", title: 'NCIT:C45290'},
    { id: 10, label: "Order", title: 'NCIT:C45287'},
    { id: 11, label: "Class", title: 'NCIT:C45280'},
    { id: 12, label: "Phylum", title: 'NCIT:C45277'},
    { id: 13, label: "Kingdom", title: 'NCIT:C45276'},
   ]);

  // create an array with edges
  var edges = new vis.DataSet([
    { from: 1, to: 3, label: 'part_of'},
    { from: 5, to: 2, label: 'part_of' },
    { from: 6, to: 5, label: 'located_in'},
    { from: 6, to: 1, label: 'participates_in'},
    { from: 4, to: 5, label: 'quality_of'},
    { from: 4, to: 6, label: 'quality_of'},
    { from: 6, to: 7, label: 'member_of'},
    { from: 6, to: 8, label: 'member_of'},
    { from: 6, to: 9, label: 'member_of'},
    { from: 6, to: 10, label: 'member_of'},
    { from: 6, to: 11, label: 'member_of'},
    { from: 6, to: 12, label: 'member_of'},
    { from: 6, to: 13, label: 'member_of'},
    { from: 7, to: 8, label: 'member_of'},
    { from: 8, to: 9, label: 'member_of'},
    { from: 9, to: 10, label: 'member_of'},
    { from: 10, to: 11, label: 'member_of'},
    { from: 11, to: 12, label: 'member_of'},
    { from: 12, to: 13, label: 'member_of'},
  ]);

  // create a network
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {};
  var network = new vis.Network(container, data, options);
</script>
