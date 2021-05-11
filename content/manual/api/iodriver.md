---
title: "IoDriver"
description: ""
lead: ""
date: 2021-04-28T16:35:20+02:00
lastmod: 2021-04-28T16:35:20+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 206
toc: true
---
This driver uploads, deletes and accesses network files.

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.convert_networkx(network_id, network)</code></b><br>

Uploads a NetworkX object to Neo4j database.

<ul>
  <li><b>network_id:</b> Name for network node</li>
  <li><b>network:</b> NetworkX object</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.delete_network(network_id)</code></b><br>

Deletes a Network node and Edge nodes that are not connected to other networks. 

<ul>
  <li><b>network_id:</b> Name for network node</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.return_networks(networks)</code></b><br>

Returns NetworkX networks from the Neo4j database.

<ul>
  <li><b>networks:</b> List of network nodes to return</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.return_taxa()</code></b><br>

Returns a list of all taxa from the Neo4j database. 
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.return_networks(networks)</code></b><br>

Returns NetworkX networks from the Neo4j database.

<ul>
  <li><b>networks:</b> List of network names to return</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.export_network(path, networks=None)</code></b><br>

Writes networks to graphML file.
If no path is given, the network is returned as a NetworkX object.
    
<ul>
  <li><b>path:</b> Filepath for writing network(s) to</li>
  <li><b>networks:</b> List of network names to write to disk</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.export_cyto(networks=None)</code></b><br>

Writes networks to Cytoscape.

    
<ul>
  <li><b>networks:</b> List of network names to export</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>IoDriver.include_nodes(nodes, name, label, verbose=True)</code></b><br>

Given a dictionary, this function tries to upload the file to the Neo4j database.
The first column of the edgelist should reflect nodes already present in the Neo4j graph database, while the second column reflects node names that will be added.
The column names are used to assign node types to the new metadata.
The dictionary should contain another dictionary of target nodes and edge weights, or only a single value (target node).
The node properties should be identical for all node dictionaries.
   
<ul>
  <li><b>nodes:</b> Dictionary of existing nodes as values with node names as keys</li>
  <li><b>name:</b> Name of variable, inserted in Neo4j graph database as type</li>
  <li><b>label:</b> Label of source node (e.g. Taxon, Specimen, Property, Experiment etc)</li>
  <li><b>verbose:</b> If true, adds logging info</li>
</ul>
</div>
<br>