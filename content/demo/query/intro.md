---
title: "Working with Python scripts"
description: ""
lead: ""
date: 2021-04-28T13:57:14+02:00
lastmod: 2021-04-28T13:57:14+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Custom queries"
weight: 201
toc: true
---

When developing custom databases, it may be helpful to run custom queries as well, and to process these queries through Python scripts. In this guide, we will use five studies that we downloaded from Qiita to show how the mako API can be used in Python scripts. All code will be either Python or Cypher, meaning it can be helpful to run it from an integrated development environment (IDE) so you can run the scripts step-by-step from the Python interpreter. 

We will use the following studies:
- The Effect of the Microbiome on Drug Metabolism, ID 11766
- The human microbiome correlates with risk factors for cardiometabolic disease across an epidemiologic transition, ID 11888
- Gut microbiome transition across a lifestyle gradient in Himalaya, ID 11947
- Swedish Infant Fecal Microbiome, ID 12021
- Microbiota and body composition during the period of complementary feeding, ID 12716

Download the files here:<br>
<a href="https://ramellose.github.io/mako_docs/demo/biomfiles.zip">biomfiles.zip</a><br>
<a href="https://ramellose.github.io/mako_docs/demo/networks.zip">networks.zip</a><br>

After downloading, unzip the files in folders named biomfiles and networks. 
