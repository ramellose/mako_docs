---
title: "Queries"
description: ""
lead: ""
date: 2021-04-29T13:43:56+02:00
lastmod: 2021-04-29T13:43:56+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Motifs"
weight: 503
toc: true
---

After defining the functions, we can run the complete script to get the EMPO annotations and access the queries. Specifically, we need to define three types of queries: we need to find all 3-node cliques, we need to find all 4-node cliques and we need to be able to filter these on weight. However, we'll need to upload the EMPO_2 annotations first. 
We can use the <code>add_metadata</code> function to do this; we need to provide a tsv file to do this. This file has Experiment nodes as one column and their EMPO_2 annotation as the other column, with Experiment and EMPO_2 as column header. 
<pre><code>
import os
import pandas as pd
from mako.scripts.io import IoDriver, add_metadata

loc = os.getcwd()

driver = IoDriver(uri='neo4j://localhost:7688',
                    user='neo4j',
                    password='test',
                    filepath=loc,
                    encrypted=False)
add_metadata(filepath=loc, location="../data/empo_annotation.tsv", driver=driver)
</pre></code>

First, we will use the driver to construct a dictionary that has the EMPO_2 files as keys and a list of taxa belonging to that EMPO_2 annotation as values. 

<pre><code>
taxa_empo = dict.fromkeys(['Animal', 'Non-saline', 'Plant', 'Saline'])
for val in taxa_empo:
    # first get experiments
    query = "MATCH (:Property {name: 'empo_2'})-[QUALITY_OF {value: '" + val + \
            "'}]-(:Experiment)--(:Specimen)--(b:Taxon) RETURN b"
    taxa = driver.query(query)
    taxa_empo[val] = set([x['b']['name'] for x in taxa])
</pre></code>

The next section of code constructs a dictionary that we can use to store the results. For each of the EMPO_2 values, this dictionary contains another dictionary with keys ranging from 1 to 14. These numbers refer to the motifs. 

<pre><code>
count_dict = dict()
for val in ['Animal', 'Non-saline', 'Plant', 'Saline']:
    count_dict[val] = dict.fromkeys(list(range(1,14)))
    for num in count_dict[val]:
        count_dict[val][num] = 0
</pre></code>

Next, we will find all posivitively- and negatively-weighted edges. While we could include the EMPO_2 annotation in the query, this would take a bit more time. Therefore, we will first query all edges and then use our EMPO_2 dictionary to assign them to different EMPO terms. 
<pre><code>
count_dict = count_motifs_empo(query="MATCH (j:Edge)--(i:Taxon) WHERE j.weight > 0 RETURN j, i",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=1)
print("Found all positively-weighted edges...")

count_dict = count_motifs_empo(query="MATCH (j:Edge)--(i:Taxon) WHERE j.weight < 0 RETURN j, i",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=2)
print("Found all negatively-weighted edges...")
</pre></code>

Next, we can look at the motifs. In this case, we are defining a three-node clique through a linear pattern. However, to do this, we need to specify four nodes, like so: A--B--C--A. Otherwise, we would miss the edge between C and A. To specify this in the query, we assign a variable <code>a</code> to the first and last node specified in the pattern; because we cannot reassign a variable within a pattern, this therefore presumes that <code>a</code> must be the same node in both positions. 

<pre><code>
# unweighted 3-node motif
count_dict = count_motifs_empo(query="MATCH p=(a:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(a) RETURN p",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=3)
print("Collected unweighted 3-node motifs...")
</pre></code>

Next, we can start looking at motifs with specific combinations of edge weights. We do this by assigning a variable to each edge and stating that the edge weight must be above or below a certain value. 

<pre><code>
# weighted 3-node motif +++
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight > 0 AND y.weight > 0 AND z.weight > 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=4)
print("Collected weighted 3-node motif +++...")
# weighted 3-node motif ---
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight < 0 AND y.weight < 0 " \
        "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=5)
print("Collected weighted 3-node motif ---...")
# weighted 3-node motif ++-
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
    "WHERE x.weight > 0 AND y.weight > 0 " \
    "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=6)
print("Collected weighted 3-node motif ++-...")
# weighted 3-node motif +--
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight > 0 AND y.weight < 0 " \
        "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=7)
print("Collected weighted 3-node motif +--...")
</pre></code>

For 4-node cliques, the query is a bit more complicated. This is because we would need to draw a single path through the clique to specify it in one line, which could get quite long. Instead, we chose to split up the query in two parts, so the first part <code>p</code> of the query specifies four nodes that need to be connected in a cycle (A--B--C--D--A), while the second and third parts <code>q</code> and <code>r</code> of the query specify the remaining connections between those four nodes, like (A--C) and (B--D). 

<pre><code>
# unweighted 4-node motif
query = "MATCH p=(a:Taxon)--(:Edge)--(b:Taxon)-" \
        "-(:Edge)--(c:Taxon)--(:Edge)--(d:Taxon)-" \
        "-(:Edge)--(a), " \
        "q=(a)--(:Edge)--(c), r=(b)--(:Edge)--(d) " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=8)
print("Collected unweighted 4-node motifs...")
</pre></code>

Just like before, this query can be extended to filter on edge weights. 

<pre><code>
# weighted 4-node motif ++++++
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight > 0 AND v.weight > 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight > 0 " \
        "RETURN p, q, r"
print("Collected weighted 4-node motif ++++++...")
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=9)
# weighted 4-node motif ------
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight < 0 AND x.weight < 0 " \
        "AND y.weight < 0 AND z.weight < 0 " \
        "RETURN p,q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=10)
print("Collected weighted 4-node motif ------...")
# weighted 4-node motif +++---
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight < 0 AND z.weight > 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=11)
print("Collected weighted 4-node motif +++---...")
# weighted 4-node motif +++---
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight < 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=12)
print("Collected weighted 4-node motif +++---...")
# weighted 4-node motif +++++-
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight > 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight > 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=13)

print("Collected weighted 4-node motif +++++-...")
</pre></code>

All that is left, is to use pandas to convert the dictionary to a dataframe that can be written to a csv file!

<pre><code>
count_data = pd.DataFrame(count_dict)
count_data.to_csv(loc + "//empo_motifs.csv")
</pre></code>
  