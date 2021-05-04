---
title: "Microbe-metabolite links"
description: ""
lead: ""
date: 2021-05-04T11:31:44+02:00
lastmod: 2021-05-04T11:31:44+02:00
draft: false
images: []
menu: 
  examples:
    parent: "IBD"
weight: 2
toc: true
---

Before we can upload any data to Neo4j, we first need to create the appropriate files to upload. 
Specifically, we need the following files: tab-delimited taxon abundance and lineage files, and an edge list that links microbes to metabolites. We will use the R package <a href="https://joey711.github.io/phyloseq/">phyloseq</a> to generate the first file and use <a href="https://cran.r-project.org/web/packages/Hmisc/Hmisc.pdf">Hmisc</a> to generate the correlations. 

In an R environment, let's first load the necessary packages and files. Make sure your working directory is set to the location where you downloaded the files. 
<pre><code>
library(Hmisc)

ibd_lineages <- read.csv("ibd_lineages.csv", row.names="X")
metabolite_features <- read.csv("ibd_metabolite_features.csv", row.names="X")
metabolite_abundances <- read.csv("ibd_metabolite_abundances.csv", row.names="X")
ibd_metadata <- read.csv("ibd_metadata.csv", row.names="X")
ibd_taxa <- read.csv("ibd_taxa.csv", row.names="X")
</pre></code>

We will remove healthy control samples from this file, since we are only interested in microbe-metabolite associations that occur in people with IBD. 

<pre><code>
ibd_samples <- row.names(ibd_metadata[ibd_metadata$Diagnosis!="Control",])
ibd_taxa <- ibd_taxa[,colnames(ibd_taxa) %in% ibd_samples]
metabolite_abundances <- metabolite_abundances[,colnames(metabolite_abundances) %in% ibd_samples]
</pre></code>

Next, let's calculate correlations between the relative abundances and the metabolites. We will use the <code>rcorr</code> function to do this. Since the function calculates all intra-matrix correlations as well, we need to 
do some additional processing to use the results. 
First, we will flatten the matrices to make a data frame that contains taxa, metabolites and the strength of the correlation. For missing Spearman correlations, this causes a missing value that we later need to remove.  
The <code>rcorr</code> function calculates all microbe-microbe and metabolite-metabolite correlations as well. Therefore, the next step is to filter these correlations; any correlation where the first position is present in the <code>metabolite_abundances</code> dataframe will be removed, while we can do the same for correlations where the second position is present in the <code>ibd_taxa</code> dataframe. We will only apply multiple-testing correction after all these irrelevant correlations are removed, so we are not correcting for tests that we only did out of convenience. 
Since there are so many potential associations, we will correct for multiple testing and only use the remaining correlations. 

<pre><code>
results <- rcorr(t(ibd_taxa), t(metabolite_abundances), type="spearman")

upper <- upper.tri(results$r)
corr_data <- data.frame(Taxon=rownames(results$r)[row(results$r)][upper], 
                        Metabolite=rownames(results$r)[col(results$r)[upper]], 
                        weight=(results$r)[upper], 
                        p = results$P[upper])

corr_data <- corr_data[!is.na(corr_data$p),]
corr_data <- corr_data[corr_data$Taxon %in% rownames(ibd_taxa),]
corr_data <- corr_data[corr_data$Metabolite %in% rownames(metabolite_abundances),]

corr_data$p <- p.adjust(corr_data$p, method="bonferroni")
corr_data <- corr_data[corr_data$p <= 0.05,]
</pre></code>

At over 7000 significant correlations remaining, this still leaves us with a large number of microbe-metabolite correlations to interpret. We will therefore include metabolite features in the Neo4j database so we can use this to make more informative analyses. To do so, we need to create a tab-delimited edge list that contains the feature data. Finally, we will write all required files to formats that can be used by mako.  

<pre><code>
chemclass <- data.frame(Metabolite=rownames(metabolite_features), Chemical.class=metabolite_features$Chemical.class)
standardmatch <- data.frame(Metabolite=rownames(metabolite_features), Standard.match=metabolite_features$Standard.match)

write.table(ibd_taxa, "ibd_taxa.tsv", sep="\t")
write.table(ibd_lineages, "ibd_lineages.tsv", sep="\t")
write.table(corr_data, "microbe_metabolite.tsv", sep="\t")
write.table(chemclass, "chemclass.tsv", sep="\t")
write.table(standardmatch, "standardmatch.tsv", sep="\t")
</pre></code>