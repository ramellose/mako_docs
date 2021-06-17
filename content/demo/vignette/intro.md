---
title: "Demo data"
description: ""
lead: ""
date: 2021-04-19T11:52:57+02:00
lastmod: 2021-04-19T11:52:57+02:00
draft: false
images: []
menu: 
  demo:
    parent: "mako"
weight: 101
toc: true
---

In this vignette, several of mako's functions will briefly be introduced with an example data set consisting of only 5 taxa and 20 samples. This data set is simple enough that most relevant nodes can be visualized in Neo4j Browser, making it feasible to follow along with all of mako's operations. 

The tables below give an overview of the data contained in the BIOM file. 

Download the files here:<br>
<a href="https://ramellose.github.io/mako_docs/demo/demo.biom">demo.biom</a><br>
<a href="https://ramellose.github.io/mako_docs/demo/demo_1.graphml">demo_1.graphml</a><br>
<a href="https://ramellose.github.io/mako_docs/demo/demo_2.graphml">demo_2.graphml</a><br>

Count table:
 OTU   | Sample1  | Sample2  | ... | Sample20 |
-------|----------|----------|-----|----------|
 OTU_1 | 0        | 0        | ... | 6        |
 OTU_2 | 5        | 1        | ... | 1        |
 OTU_3 | 0        | 0        | ... | 0        |
 OTU_4 | 2        | 1        | ... | 0        |
 OTU_5 | 0        | 1        | ... | 0        |
 
 Taxonomy table:
 
  OTU   | Phylum       | Class             |  Order          | Family           |  Genus        |  Species      |
  ------|--------------|-------------------|-----------------|------------------|---------------|---------------|
  OTU_1 |Proteobacteria|Gammaproteobacteria|Enterobacteriales|Enterobacteriace  |Escherichia    |               |
  OTU_2 |Firmicutes    |Clostridia         |Halanaerobiales  |Halobacteroidaceae|Sporohalobacter|lortetii       |
  OTU_3 |Euryarchaeota |Methanomicrobia    |Methanosarcinales|Methanosarcinaceae|Methanosarcina |               |
  OTU_4 |Firmicutes    |Clostridia         |Halanaerobiales  |Halanaerobiaceae  |Halanaerobium  |saccharolyticum|
  OTU_5 |Proteobacteria|Gammaproteobacteria|Enterobacteriales|Enterobacteriace  |Escherichia    |               |

Sample metadata (BarcodeSequence and LinkerPrimerSequence not shown):

Sample     | BODY_SITE | Description |
-----------|-----------|-------------|
Sample1-10 | gut       | human gut   |
Sample11-20| skin      | human skin  |

Edge list: 

Network | Target | Source | Weight |
--------|--------|--------|--------|
demo_1  | OTU_1  | OTU_2  | 1      |
demo_1  | OTU_2  | OTU_5  | 1      |
demo_1  | OTU_3  | OTU_4  | -1     |
demo_1  | OTU_1  | OTU_5  | 1      |
demo_2  | OTU_1  | OTU_2  | 1      |
demo_2  | OTU_2  | OTU_5  | 1      |
demo_2  | OTU_1  | OTU_5  | -1     |


