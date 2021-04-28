---
title: "Biom2Neo"
description: ""
lead: ""
date: 2021-04-28T16:34:53+02:00
lastmod: 2021-04-28T16:34:53+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 5
toc: true
---

This driver contains functions for writing BIOM files to the database,
and also for writing BIOM files from the database to disk.
 
<div style="outline:0.01em solid black; padding:10px;">
<b><code>Biom2Neo.convert_biom(biomfile, exp_id, obs=True)</code></b><br>

Stores a BIOM object in the database.
To speed up this process, all data from the BIOM object is first converted to dictionaries or lists that can be used in parameterized batch queries.
If obs is set to false, all taxa are only connected to a single "mock" sample.
This can lead to a rapid speed-up for data set uploading, if sample counts are not necessary.

<ul>
  <li><b>biomfile:</b> BIOM object</li>
  <li><b>exp_id:</b> Label of experiment used to generate BIOM file</li>
  <li><b>obs:</b> Relationships between samples and taxa are only created if obs is set to True</li>
</ul>
</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>Biom2Neo.convert_taxonomy(taxonomy_table, exp_id)</code></b><br>

Stores a taxonomy dataframe in the database.
To speed up this process, all data from the taxonomy table is first converted to dictionaries or lists that can be used in parameterized batch queries.
    

<ul>
  <li><b>taxonomy_table:</b> BIOM object</li>
  <li><b>exp_id:</b> Pandas dataframe of taxonomy</li>
  <li><b>exp_id:</b> Label of experiment used to generate taxonomy file</li>
</ul>
</div>
<br>
