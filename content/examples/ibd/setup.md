---
title: "Populating the database"
description: ""
lead: ""
date: 2021-05-04T09:37:13+02:00
lastmod: 2021-05-04T09:37:13+02:00
draft: false
images: []
menu: 
  examples:
    parent: "IBD"
weight: 203
toc: true
---

For this section of the case study, we will interact with a running Neo4j database. If you do not have such a database available, please take a look at the <a href="/neo4j/introduction/intro">Neo4j section of this web page</a> to learn how to set up one locally or via Docker. 

To upload our data, we need to open a terminal and navigate to the folder where we stored the files from the previous section. We can upload all files using the <code>neo4biom</code> and <code>io</code> modules. Remember to adjust the address and password if those are different for your Neo4j instance!

<pre><code>
mako neo4biom -u neo4j -p test -a neo4j://localhost:7688 -cf -count ibd_taxa.tsv 
mako neo4biom -cf -tax ibd_lineages.tsv
</pre></code>

Next, we will upload the relationships between species and metabolites. Since the metabolites are all strings, they will be uploaded as separate <code>Metabolite</code> nodes (since Metabolite is the column name in the file). We need to upload files in the correct order, so that the first column always contains nodes that already exist in the database. 

<pre><code>
mako io -cf -meta microbe_metabolite.tsv
mako io -cf -meta chemclass.tsv
mako io -cf -meta standardmatch.tsv
</pre></code>

After completing the above tasks, you should be able to conveniently query all metabolites in the database. For example, we can easily find the chemical classes that certain metabolite clusters belong to. 

<figure>
  <img src="/images/ibd_metabolites.PNG" alt="Screenshot of Neo4j Browser showing Cypher query outcome with Metabolite nodes." width="600"> 
  <figcaption>Figure 1: Screenshot of Neo4j Browser showing Cypher query outcome with Metabolite nodes.</figcaption>
</figure>
