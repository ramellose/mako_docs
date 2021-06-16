---
title: "A literature-curated network"
description: ""
lead: ""
date: 2021-05-06T09:38:46+02:00
lastmod: 2021-05-06T09:38:46+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Validation"
weight: 301
toc: true
---

Many interactions between microbes are mediated through metabolites. Microbes can secrete metabolites like lactate, which can then be used by others as a carbon source. However, with only metabarcoding data, it is impossible to see metabolite fluxes or expression of genes that are required to facilitate such fluxes. 

In this case study, we are going to import a literature-curated network of metabolite-driven microbial interactions. We will use this network to find associations in a different association network that could possibly be driven by specific metabolic interactions. We will use the network curated by Sung et al. (2017) and first convert this to a format mako can work with. Then, we will compare it to a gut association network we generated previously as part of <a href="/examples/qiita/intro">our Qiita dataset</a>. 

If you have not done so yet, download the literature-curated network from <a href="https://www.nature.com/articles/ncomms15393#Sec16">Sung et al. (2017)</a>. We will work with one of the XML files in Supplementary Data 4. 

For our association network, we will work with a network that we previously generated using data from Qiita, specifically <a href="https://qiita.ucsd.edu/study/description/11766">The Effect of the Microbiome on Drug Metabolism, ID 11766</a>. The network has been generated with FlashWeave, with the heterogeneous mode set to false and the minimum number of observations to 10. Since most taxa did not have species assignments, they were merged by genus. The data was then filtered so all taxa with less than 20% prevalence were moved to a synthetic "Bin" taxon.  <br><br>
For convenience, pre-processed files are available below:<br>
<a href="/demo/11766.biom">11766.biom</a><br>
<a href="/demo/11766.txt">11766.txt</a><br>

<a href="https://www.nature.com/articles/ncomms15393">Sung, J., Kim, S., Cabatbat, J. J. T., Jang, S., Jin, Y. S., Jung, G. Y., ... & Kim, P. J. (2017). Global metabolic interaction network of the human gut microbiota for context-specific community-scale analysis. <i>Nature communications, 8</i>(1), 1-12.</a>