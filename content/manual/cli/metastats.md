---
title: "mako metastats"
description: ""
lead: ""
date: 2021-04-20T11:34:02+02:00
lastmod: 2021-04-20T11:34:02+02:00
draft: false
images: []
menu: 
  manual:
    parent: "CLI"
weight: 107
toc: true
---

The <code>metastats</code> module can carry out some basic operations on metadata. It can agglomerate networks to higher taxonomic levels (so all edges are merged to Family-level associations, for example), or it can carry out basic statistics. Specifically, it can calculate Spearman correlations between taxon abundances and quantitative metadata, and hypergeometric tests for qualitative metadata. 

The edge agglomeration works by finding patterns, e.g. genus--taxon--edge--taxon--genus. If two edges have the same genus at both sides and matching weight, they can be merged together. 

<ul>
  <li><code>-net</code> One or more Network names to be used by <code>-agglom</code>, by default all networks</li>
  <li><code>-w</code> If flagged, edge weights are not taken into account</li>
  <li><code>-agglom</code> Choose a taxonomic level (species, genus, family, order, class, phylum) to agglomerate networks to</li>
  <li><code>-var</code> Specify "all" to carry out tests for all Property nodes connected to Specimen nodes, or one or more variable names to only test those variables</li>
</ul>