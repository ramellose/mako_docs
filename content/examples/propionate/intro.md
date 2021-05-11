---
title: "Short chain fatty acids"
description: ""
lead: ""
date: 2021-04-29T13:44:40+02:00
lastmod: 2021-04-29T13:44:40+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Propionate"
weight: 601
toc: true
---

The human gut microbiome is capable of fermenting carbohydrates into short-chain fatty acids, which have been linked to human health. One of those short-chain fatty acids is propionate. In their review on propionate production, Louis and Flint (2017) provide a brief overview of the bacterial species that have the metabolic capacity to contribute to propionate formation. Not all bacteria are able to degrade all substrates, or to carry out the entire pathway. Moreover, propionate production may occur through different intermediates, succinate and 1,2-propanediol, meaning that different molecules and enzymes are involved. 

In this case study, we are going to take a closer look at the 1,2-propanediol pathway. Most bacterial species only support half of the pathway: they can degrade a substrate, like fucose, rhamnose or other monosaccharides, so that the  1,2-propanediol intermediate is formed. However, they cannot support the further production of propionate from this intermediate. A few bacterial species can carry out the entire pathway, while another few are able produce propionate from 1,2-propanediol, but unable to degrade monosaccharide substrates. The complete overview of this pathway is given in Figure 3 of the review by Louis and Flint (2017). 

In this example, we will use the Neo4j database to enumerate associations between species that, combined, have the ability to carry out the full pathway. First, we will show what queries can be used to find these species; next, we will show how we visualized the associations using UpsetR (Conway et al., 2017). We assume that a running Neo4j database with all 60 data sets is already available (see <a href="../../qiita/intro">the Qiita case study for more information</a>). 

<a href="https://academic.oup.com/bioinformatics/article/33/18/2938/3884387">Conway, J. R., Lex, A., & Gehlenborg, N. (2017). UpSetR: an R package for the visualization of intersecting sets and their properties. <i>Bioinformatics, 33</i>(18), 2938-2940.</a>

<a href="https://sfamjournals.onlinelibrary.wiley.com/doi/10.1111/1462-2920.13589">Louis, P., & Flint, H. J. (2017). Formation of propionate and butyrate by the human colonic microbiota. <i>Environmental microbiology, 19</i>(1), 29-41.</a>