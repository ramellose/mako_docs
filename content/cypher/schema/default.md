---
title: "Default nodes and relationships"
description: ""
lead: ""
date: 2021-04-21T16:29:43+02:00
lastmod: 2021-04-21T16:29:43+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Schema"
weight: 303
toc: true
---

Many of the nodes and relationships have properties that represent specific characteristics. The overview below contains a description of each node or relationship, its ontology term and any properties that the item has if default import functions are used. 

<h5>Edge - NCIT:C75923</h5>
The <code>Edge</code> node is one of the most important nodes of mako and supports most of its functionality. While it is possible to connect <code>Taxon</code> nodes directly, the <code>Edge</code> node can be connected separately to <code>Network</code> nodes or <code>Property</code> nodes, so that more complicated <code>Edge</code> metadata is possible. For example, <code>Edge</code> nodes could be connected to a <code>Network</code> node named Literature if they are identified via a literature analysis. Hence, this implementation expressly facilitates network meta-analyses. 
<ul>
<li><code>name</code> Edge nodes normally are assigned a universally unique identifier (UUID) as a name property, since edge lists and matrix formats do not contain edge identifiers. </li>
<li><code>Weight</code> If available, Edge nodes are also assigned a weight property. Since edge weights are usually not directly comparable across network inference methods, it is recommended to use a binary representation of 1 and -1 for positively- and negatively- weighted edges. </li>
</ul>

<h5>Experiment - NCIT:C42790</h5>
The <code>Experiment</code> node connects all <code>Specimen</code> nodes to a single file.
<ul>
<li><code>name</code> The name for the Experiment node is taken from the filename of the imported file, but it can also be adjusted manually.  </li>
</ul>

<h5>Network - NCIT:C61377</h5>
The <code>Network</code> node connects all <code>Edge</code> nodes to a single network. An alternative version of <code>Network</code> nodes is also available; these have the <code>Set</code> label and are used to indicate results of network operations. 
<ul>
<li><code>name</code> The name for the Network node is taken from the filename of the imported file, but it can also be adjusted manually.  </li>
</ul>

<h5>Property - NCIT:C20189</h5>
<code>Property</code> nodes are nodes that can be used to query specific metadata. These can be connected to any other node, but default imports connect them to <code>Specimen</code> and <code>Taxon</code> nodes. 
<ul>
<li><code>name</code> The name for the Property node is taken from the column name (if table-like import). For example, a column with pH values will lead to one pH property being generated. </li>
</ul>

<h5>Specimen - NCIT:C19157</h5>
<code>Specimen</code> nodes represent specimens or samples collected for an experiment. <ul>
<li><code>name</code> The name for the Specimen node is taken from whatever sample identifier is used by the file, e.g. column names for standard count tables. </li>
</ul>

<h5>Taxon - NCIT:C40098</h5>
<code>Taxon</code> nodes usually represent OTUs or ASVs, but can also represent any other biological unit. <ul>
<li><code>name</code> The name for the Taxon node is taken from whatever taxon identifier is used by the file, e.g. row names for standard count tables. </li>
</ul>

<h5>Species, Genus, Family, Order, Class, Phylum, Kingdom</h5>
NCIT:C45293, NCIT:C45292, NCIT:C45290, NCIT:C45287, NCIT:C45280, NCIT:C45277, NCIT:C45276 
<br>
These nodes represent taxonomic values for these specific taxonomic levels. 
<code>Taxon</code> nodes usually represent OTUs or ASVs, but can also represent any other biological unit. <ul>
<li><code>name</code> The name for taxonomy nodes is the value usually represented in taxonomy tables. For example, the <code>Genus</code> node for <i>Escherichia coli</i> will have <i>Escherichia</i> as a name. When tables contain only a prefix (e.g. g__), no node is created. </li>
</ul>

<h5>LOCATED_IN</h5>
Relationships connecting <code>Taxon</code> nodes to <code>Specimen</code> nodes. 
<ul>
<li><code>count</code> Value of count or abundance table for a specific taxon in a specific specimen. </li>
</ul>

<h5>MEMBER_OF</h5>
Relationships connecting <code>Taxon</code> nodes to taxonomy nodes (<code>Species</code>, <code>Genus</code>, <code>Family</code>, <code>Order</code>, <code>Class</code>, <code>Phylum</code> and <code>Kingdom</code>), and also taxonomy nodes to each other. These relationships form acyclic trees with <code>Kingdom</code> as the root and therefore mimic taxonomic trees. By directly connecting <code>Taxon</code> nodes to taxonomy nodes, queries can access those directly. 

<h5>PARTICIPATES_IN</h5>
Relationships connecting <code>Taxon</code> nodes to <code>Edge</code> nodes. These relationships are currently undirected, so <code>Taxon</code> nodes always participate in an edge, rather than being affected by another taxon. 

<h5>PART_OF</h5>
Relationships connecting <code>Sample</code> nodes to <code>Experiment</code> nodes and <code>Edge</code> nodes to <code>Network</code> nodes. These relationships therefore indicate a hierarchy of file structures. 

<h5>QUALITY_OF</h5>
Relationships connecting nodes to <code>Property</code> nodes. Usually, these relationships connect <code>Taxon</code> and <code>Specimen</code> nodes to <code>Property</code> nodes, but other nodes can be connected to <code>Property</code> nodes as well. 
<ul>
<li><code>value</code> Value of the Property node. For example, if pH values per sample are uploaded to the database, one pH Property node is generated and all <code>QUALITY_OF</code> relationships contain the pH value for that specific Specimen node.</li>
</ul>
