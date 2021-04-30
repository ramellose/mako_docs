---
title: "Making an Upset plot"
description: ""
lead: ""
date: 2021-04-29T13:48:00+02:00
lastmod: 2021-04-29T13:48:00+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Propionate"
weight: 3
toc: true
---

To visualize the results, we need to visualize associations between genera, and the number of times these links were found in the database. The matrix layout under the barplot allows <a href="http://gehlenborglab.org/research/projects/upsetr/"><code>UpsetR</code></a> to effectively visualize these links. 

To run <code>UpsetR</code>, we first need to process the data we collected previously, so that it is in a format that <code>UpsetR</code> can work with. Specifically, we will make a column filled with zeroes for each genus. Each association is encoded as a row. Values in the row are set to 1 depending on the genera participating in that association. We will also remove the other columns, since those cannot be used directly by <code>UpsetR</code>, but need to be added via a <code>metadata</code> dataframe. 

<pre><code>
library(UpSetR)
library(viridis)

data <- read.csv("propionate_matches.csv", row.names="X", stringsAsFactors=FALSE)

upset_data <- data
for (target in data$Sugar.degradation){
  upset_data[[target]] <- 0
}
for (target in data$Propionate.formation){
  upset_data[[target]] <- 0
}
upset_data$Sugar.degradation <- NULL
upset_data$Propionate.formation <- NULL
upset_data$Network <- NULL

for (i in 1:nrow(data)){
  row <- data[i,]
  sugar_degrader <- data$Sugar.degradation[i]
  upset_data[[sugar_degrader]][i] <- 1
  propionate_producer <- data$Propionate.formation[i]
  upset_data[[propionate_producer]][i] <- 1
}
</pre></code>

Next, we will create the <code>metadata</code> dataframe, so we can represent the molecules linked to each of the genera according to literature. We will also define some colorblind-friendly colours.  
<pre><code>
metadata <- data.frame(Sets=c("Lactobacillus",
                              "Bacteroides",
                              "Escherichia",
                              "Blautia",
                              "Anaerostipes",
                              "Roseburia",
                              "Clostridium",
                              "Listeria"))
metadata$Substrate <- c('lacp',
                        'fuc',
                        'fucother',
                        'fucp',
                        'fuc',
                        'fucp',
                        'other',
                        'fucp')
# need to manually define sets
colours <- viridis(5)
</pre></code>

The last part is then to create the Upset plot and save it to a PDF file. 

<pre><code>
pdf(file="Figure2b_propionate_matches.pdf", width=6, height=5, onefile=FALSE) 
upset(upset_data, nsets=20, 
      set.metadata = list(data=metadata, 
      plots=list(list(type="matrix_rows", column="Substrate", alpha=0.5,
      colors=c(fuc = colours[[1]], 
      fucp = colours[[2]],
      lacp = colours[[3]],
      other = colours[[4]],
      fucother = colours[[5]])))))
dev.off()
</pre></code>

The results should look similar to the image below, although these values are only shown for 5 Animal data sets. Here, <i>Roseburia</i> had the most associations that could potentially be linked to propionate production. We later manually added a legend that visualized the propionate pathway. 

<figure>
  <img src="/images/propionate.png" alt="An Upset plot showing counts of propionate associations for five gut microbiome studies." width="400"> 
  <figcaption>Figure 1: Counts of propionate associations for five gut microbiome studies.</figcaption>
</figure>
