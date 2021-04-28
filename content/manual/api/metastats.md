---
title: "MetastatsDriver"
description: ""
lead: ""
date: 2021-04-28T16:36:04+02:00
lastmod: 2021-04-28T16:36:04+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 8
toc: true
---

This driver extracts nodes and edges from the database that are required
for the operations defined in the metastats module.
    
<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.agglomerate_networks(level=None, weight=True, networks=None)</code></b>

Agglomerates to specified taxonomic level, or, if no level is specified,
over all levels. Edges are agglomerated based on similarity
at the specified taxonomic level. If 'weight' is set to True,
edges are only agglomerated if their weight matches.
The stop condition is the length of the pair list;
as soon as no pair meets the qualification, agglomeration is terminated.
By default, agglomeration is done separately
per network in the database, so each network gets an agglomerated version.

The networks parameter can be both a dict and a list.
If it is a dict, the keys are the new network names, the values the old names.

Pseudocode representation:
1. Duplicate networks
2. For each edge pair (taxon-level)-taxon-taxon-(taxon-level)
    3. Create new edge
    4. Delete edge pair
  
<ul>
  <li><b>level:</b> Taxonomic level to agglomerate to</li>
  <li><b>weight:</b> If True, takes edge weight sign into account</li>
  <li><b>networks:</b> If specified, only these networks are agglomerated</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.copy_network(source_network, new_network)</code></b>

Copies a network node and its edges.
The network node name is new_network, edge IDs are generated with uuid4.
The weights of the edges are not copied, only the signs.

  
<ul>
  <li><b>source_network:</b> Source network name</li>
  <li><b>new_network:</b> New network name</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.get_pairlist(level, weight, network)</code></b>

Returns an edge pair. 
A pair is defined as two edges linked to taxonomic nodes that have the same taxonomic assignment at the specified level, e.g. Nitrobacter-edge-Nitrosomonas. 
   
  
<ul>
  <li><b>level:</b> Taxonomic level to identify a pair</li>
  <li><b>weight:</b> If True, specifies that edge weights should have the same sign</li>
  <li><b>network:</b> Name of network that the pairs should belong to</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.agglomerate_pair(pair, level, weight, network)</code></b>

For one pair, as returned by <code>get_pairlist</code>, this function creates new agglomerated nodes, deletes old agglomerated nodes, and chains taxonomic nodes to the new agglomerated nodes. Morever, the two old edges are deleted and replaced by a new edge.
  
<ul>
  <li><b>pair:</b> </li> List containing transaction results of query for pair
  <li><b>level:</b> Taxonomic level to identify a pair</li>
  <li><b>weight:</b> If True, specifies that edge weights should have the same sign</li>
  <li><b>network:</b> Name of network that the pairs should belong to</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.get_taxlist(level, network)</code></b>

Returns taxon pairs. 
A taxon pair is a list containing two edges linked to identical taxonomy, e.g. edge-taxon-Nitrobacter-taxon-edge. 

  
<ul>
  <li><b>level:</b> Taxonomic level to identify a pair</li>
  <li><b>network:</b> Name of network that the pair should belong to</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.agglomerate_taxa(pair, level, network)</code></b>

For one pair, as returned by <code>get_taxlist</code>, this function merges nodes with similar taxonomy but different edges together.
Old nodes are linked to the new agglomerated node, except for Agglom_Taxon; in that case,links to the ancestral nodes are generated.

<ul>
  <li><b>pair:</b> </li> List containing transaction results of query for pair
  <li><b>level:</b> Taxonomic level to identify a pair</li>
  <li><b>weight:</b> If false, merges edges with different weights</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.associate_samples(label, null_input=None)</code></b>

To test the hypothesis that taxa are associated with specific sample properties,
the following tests are performed:
1. For qualitative variables, a hypergeometric test is performed;
how many edges do we expect by chance?
2. For quantitative variables, Spearman correlation is performed.
Because this is a hypothesis-generating tool,
multiple-testing correction should be applied with care.
  
<ul>
  <li><b>label:</b> Label of property (e.g. pH) to query</li>
  <li><b>null_input:</b> If missing values are not specified as NA, specify the NA input here</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>MetastatsDriver.associate_taxon(taxon, null_input, properties)</code></b>

Tests whether specific sample properties can be associated to a taxon.

<ul>
  <li><b>taxon:</b> Name of a taxon</li>
  <li><b>null_input:</b> If missing values are not specified as NA, specify the NA input here</li>
  <li><b>properties:</b> List specifying names of properties to query</li>
</ul>
</div>
<br>
