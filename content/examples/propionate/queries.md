---
title: "Finding genera"
description: ""
lead: ""
date: 2021-04-29T13:48:30+02:00
lastmod: 2021-04-29T13:48:30+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Propionate"
weight: 602
toc: true
---

To run the queries on the Neo4j database, we first need to set up a driver. This can be any driver, since all drivers have the ability to run queries. 

<pre><code>
import os
import pandas as pd
from mako.scripts.io import IoDriver

loc = os.getcwd()

driver = IoDriver(uri='neo4j://localhost:7688',
                    user='neo4j',
                    password='test',
                    filepath=loc,
                    encrypted=False)
</pre></code>

First, let's specify which bacteria are able to carry out certain steps. Since the database doesn't contain species information, only genus-level assignments, we will go with this information. 

For each substrate, we will make a list of genera that could be able to degrade this. 
There are some bacteria that can degrade fucose or rhamnose, but not carry out the final steps to produce propionate. We will split these up in a list. Finally, we will make a list containing all genera that could possibly carry out propionate formation from propionyl-CoA. 

<pre><code>
fuc = ['g__Bacteroides', 'g__Anaerostipes', 'g__Escherichia']
fuc_coa = ['g__Roseburia', 'g__Blautia', 'g__Salmonella', 'g__Listeria']
lac = ['g__Lactobacillus']
sacc = ['g__Clostridium', 'g__Escherichia', 'g__Saccharomyces']
coa = ['g__Eubacterium', 'g__Lactobacillus']

fuc_upstream = fuc.copy()
fuc_upstream.extend(fuc_coa)

all_coa = fuc_coa.copy()
all_coa.extend(coa)    
</pre></code>

Next, we can query each of these patterns. We'll organize them by substrate, since all substrates eventually need to pass the propionyl-CoA step. We are going to look for patterns that match <code>Edge</code> nodes and that filter on the name of the <code>Genus</code> node. 

<pre><code>
# fuc motifs
fuc_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(fuc_upstream) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected fucose motifs...")
# lac motifs
lac_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(lac) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected lactose motifs...")
# sacc motifs
sacc_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(sacc) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected other monosaccharid motifs...")

driver.close()
</pre></code>

We can take these results and process them so they can be stored as a dataframe. Dictionaries are a convenient approach; the below script creates a dictionary that describes the substrate sugar, the name of the substrate degrader, the name of the propionate producer and the name of the source network. 

<pre><code>
results = list()
for motif in lac_motifs:
    results.append({'Sugar': 'Lactate, fucose or rhamnose',
                    'Sugar degradation': motif['p'][0]['name'][3:],
                    'Network': motif['n']['name'],
                    'Propionate formation': motif['p'][8]['name'][3:]})
for motif in fuc_motifs:
    if motif['p'][4]['name'] not in all_edges:
        results.append({'Sugar': 'Fucose or rhamnose',
                        'Sugar degradation': motif['p'][0]['name'][3:],
                        'Network': motif['n']['name'],
                        'Propionate formation': motif['p'][8]['name'][3:]})
for motif in sacc_motifs:
    if motif['p'][4]['name'] not in all_edges:
        results.append({'Sugar': 'Most monosaccharides',
                        'Sugar degradation': motif['p'][0]['name'][3:],
                        'Network': motif['n']['name'],
                        'Propionate formation': motif['p'][8]['name'][3:]})
</pre></code>

The last step is to convert the dictionary to a dataframe. 

<pre><code>
propionate_motifs = pd.DataFrame(results)
propionate_motifs.to_csv(loc + "//propionate_matches.csv")
</pre></code>