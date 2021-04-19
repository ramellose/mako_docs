---
title: "Calculate metadata correlations"
description: ""
lead: ""
date: 2021-04-19T11:49:26+02:00
lastmod: 2021-04-19T11:49:26+02:00
draft: false
images: []
menu: 
  demo:
    parent: "demo"
weight: 6
toc: true
---

The command below carries out hypergeometric tests to see if the metadata (skin vs gut) is linked to specific taxa. Note that this is not a robust way to estimate correlations between taxa and metadata and dedicated, more appropriate statistical methods should be used for this purpose. The <code>-var all</code> parameter tells mako to run the tests across all variables. 

<code>mako metastats -fp local_filepath -cf -var all</code>

If you access the Neo4j Browser (<a href="http://localhost:7475/browser/">http://localhost:7475/browser/</a>) and run the following query, you should be able to access all taxa that were linked to the skin or gut samples via the hypergeometric test:

<code>MATCH p=(n:Taxon)--(:Property) RETURN p LIMIT 50</code>

<img src="/images/demo_4.PNG" alt="Metadata links to taxa." width="600"> 
