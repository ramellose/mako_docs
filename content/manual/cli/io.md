---
title: "mako io"
description: ""
lead: ""
date: 2021-04-20T11:33:45+02:00
lastmod: 2021-04-20T11:33:45+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 105
toc: true
---
The <code>io</code> module can be used to write network files to a Neo4j database according to mako's database schema. Networks can be imported as graphml files, gml files or as weighted edge lists (text files with three columns: source nodes, target nodes and the edge weights). The <code>-fp</code> prefix contains the shared file path, so there is no need to write the full file path, partial file paths or just filenames are sufficient if <code>-fp</code> is used. 

The <code>io</code> module also has options for adding extra metadata to the Neo4j database. If a tab-delimited edge list is supplied with existing nodes in the 1st column and new properties in the 2nd column, this is used to create a new Property node with relationships containing property values.If all property values are strings, a new node is made with a label identical to the column value and the node name as the string value. 

Finally, the module can delete and export networks or derived sets (generated with the <code>netstats</code> module) to a running instance of Cytoscape or to a graphml file. To run these operations, the <code>-net</code> parameter should be given names of Network or Set names in the Neo4j database.

<ul>
  <li><code>-net</code> One or more (filepaths of) network files, or Network / Set names</li>
  <li><code>-del</code> Name(s) of Network or Set node(s) that should be deleted</li>
  <li><code>-fasta</code> Name(s) of FASTA files, e.g. GreenGenes FASTA files</li>
  <li><code>-cyto</code> If flagged, exports networks listed in <code>-net</code> to Cytoscape</li>
  <li><code>-meta</code> One or more tab-delimited files with node metadata (as a 2-column table). Column names are used to match node labels</li>
  <li><code>-w</code> If flagged, writes networks listed in <code>-net</code> to graphml</li>
</ul>
