---
title: "HMA-LMA status"
description: ""
lead: ""
date: 2021-05-07T10:47:15+02:00
lastmod: 2021-05-07T10:47:15+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Sponges"
weight: 101
toc: true
---

Marine sponges, also known as Porifera, are a highly diverse clade of animals known for their ability to host complex microbial communities. Generally, these sponges can be categorized as either high microbial abundance (HMA) or low microbial abundance (LMA), depending on the density of the microbial communities they harbour (Gloeckner et al., 2014). Relatively little is known about these communities, since most members are uncultivated. 

In this case study, we are going to integrate association networks derived from different sponge orders with a list of taxa previously found to be related to the HMA-LMA dichotomy. We will use abundance data from the sponge microbiome project (Moitinho-Silva et al., 2017a) and a taxon list derived from a study evaluating the HMA-LMA status with machine learning (Moitinho-Silva et al., 2017b). 

We have pre-processed BIOM files in advance and constructed association networks with FlashWeave (heterogeneous set to false, minimum observations set to 10). These are available via the zip files below. We have also downloaded the supplementary Table 5 from (Moitinho-Silva et al., 2017b) and processed this so the files can be imported by mako. To do so, we assigned phylogenetic levels as either HMA or LMA depending on the sponge type where they were most abundant on average.  Download all these files below: <br><br>
<a href="/demo/sponge_biomfiles.zip">sponge_biomfiles.zip</a><br>
<a href="/demo/sponge_networks.zip">sponge_networks.zip</a><br>
<a href="/demo/sponge_class.tsv">sponge_class.tsv</a><br>
<a href="/demo/sponge_phylum.tsv">sponge_phylum.tsv</a><br>

<a href="https://www.journals.uchicago.edu/doi/full/10.1086/BBLv227n1p78">Gloeckner, V., Wehrl, M., Moitinho-Silva, L., Gernert, C., Schupp, P., Pawlik, J. R., ... & Hentschel, U. (2014). The HMA-LMA dichotomy revisited: an electron microscopical survey of 56 sponge species. <i>The Biological Bulletin, 227</i>(1), 78-88.</a>

<a href="https://academic.oup.com/gigascience/article/6/10/gix077/4082886">Moitinho-Silva, L., Nielsen, S., Amir, A., Gonzalez, A., Ackermann, G. L., Cerrano, C., ... & Thomas, T. (2017a). The sponge microbiome project. <i>Gigascience, 6</i>(10), gix077.</a>

<a href="https://www.frontiersin.org/articles/10.3389/fmicb.2017.00752/full">Moitinho-Silva, L., Steinert, G., Nielsen, S., Hardoim, C. C., Wu, Y. C., McCormack, G. P., ... & Hentschel, U. (2017b). Predicting the HMA-LMA status in marine sponges by machine learning. <i>Frontiers in microbiology, 8</i>, 752.</a>