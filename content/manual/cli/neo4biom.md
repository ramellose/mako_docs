---
title: "mako neo4biom"
description: ""
lead: ""
date: 2021-04-20T11:33:36+02:00
lastmod: 2021-04-20T11:33:36+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 104
toc: true
---

The <code>neo4biom</code> module can be used to write BIOM files or tab-delimited files to a Neo4j database according to mako's database schema. The <code>-fp</code> prefix contains the shared file path, so there is no need to write the full file path, partial file paths or just filenames are sufficient if <code>-fp</code> is used. 
If the <code>-o</code> flag is provided, BIOM files are uploaded without counts (so only taxonomy and metadata is uploaded). Instead, a proxy specimen node is included. This can lead to rapid speed increases, especially for larger data sets, as these can contain thousands of counts. 
For each file, an Experiment node is created that matches the filename. If more than one tab-delimited file is provided, metadata files should be in the same order as the count table. Instead of providing a count table with metadata, it also possible to create Taxon nodes from taxonomy tables alone. Additionally, the <code>neo4biom</code> module provides a function for deleting a single Experiment node; disconnected Taxon nodes no longer present in specimens are also removed. 

<ul>
  <li><code>-biom</code> One or more (filepaths of) BIOM files</li>
  <li><code>-count</code> One or more tab-delimited count tables (samples as columns)</li>
  <li><code>-tax</code> One or more tab-delimited taxonomy tables</li>
  <li><code>-tm</code> One or more tab-delimited files with taxon metadata</li>
  <li><code>-sm</code> One or more tab-delimited files with sample metadata</li>
  <li><code>-del</code> Name(s) of Experiment node(s) that should be deleted</li>
  <li><code>-o</code> If flagged, BIOM files are uploaded without count data</li>
</ul>