---
title: "Sponge networks"
description: ""
lead: ""
date: 2021-05-07T10:49:39+02:00
lastmod: 2021-05-07T10:49:39+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Sponges"
weight: 102
toc: true
---

For this section of the case study, we will interact with a running Neo4j database. If you do not have such a database available, please take a look at the <a href="/neo4j/introduction/intro">Neo4j section of this web page</a> to learn how to set up one locally or via Docker. 

To upload our data, we need to open a terminal and navigate to the folder where we stored the files from the previous section. Make sure to unzip the zip files with all BIOM and network files into folders with the same names. We can then upload all files using the <code>neo4biom</code> and <code>io</code> modules. Remember to adjust the address and password if those are different for your Neo4j instance!

Note that the <code>-biom</code> and <code>-net</code> flags only need the folder name; they will simply try to import every file present in this folder. 

<pre><code>
mako neo4biom -u neo4j -p test -a neo4j://localhost:7688 -cf -biom sponge_biomfiles
mako io -cf -net sponge_networks
</pre></code>

Next, we will upload the files that indicate HMA and LMA associations. These need to have the appropriate column names, so that we create only one HMA and one LMA node and we connect these to <code>Class</code> and <code>Phylum</code> nodes. Not all phylogenetic groups found by Moitinho-Silva et al. are actually present in these networks; this is okay, we will be able to query the ones that are. 

<pre><code>
mako io -cf -meta sponge_class.tsv
mako io -cf -meta sponge_phylum.tsv
</pre></code>

After completing the above tasks, you should be able to find phylogenetic levels that are linked to HMA or LMA status. 

<figure>
  <img src="/images/sponge_type.PNG" alt="Screenshot of Neo4j Browser showing Cypher query outcome with Type nodes." width="600"> 
  <figcaption>Figure 1: Screenshot of Neo4j Browser showing Cypher query outcome with Type nodes.</figcaption>
</figure>

