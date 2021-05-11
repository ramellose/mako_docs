---
title: "Importing the literature network"
description: ""
lead: ""
date: 2021-05-06T09:38:55+02:00
lastmod: 2021-05-06T09:38:55+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Validation"
weight: 303
toc: true
---

Before we can upload the literature network to Neo4j, we first need to create the appropriate files to upload. 
Specifically, we need to convert the XML file to a metadata file that can be imported easily. We also need to make sure the taxon identifiers match. The NJS16 network only has species identifiers, not the full taxonomy, so we will take the taxonomy of nodes in the association network and match this to the NJS16 identifiers. 

In an Python environment, let's first load the necessary packages and files. Make sure to set the <code>loc</code> parameter to the location where you stored the files. 

<pre><code>
import networkx as nx
from mako.scripts.io import IoDriver
import os
import xml.etree.ElementTree as et
import pandas as pd

loc = os.getcwd()
</pre></code>

Next, we will use the <code>xml</code> package to parse the NJS16 file. We are going to simplify interaction names a bit, to make later queries a bit simpler. Finally, we will construct a list of dictionaries that contains all the information we need to upload to Neo4j. 

<pre><code>
xtree = et.parse(loc + "/NJS16_MetabolicActivity_as_EdgeAttribute.xml")
xroot = xtree.getroot()

node_dict = {}
edge_rows = []

# Simplify interaction types for Neo4j relationship use
interaction_names = {'Consumption (import)': 'consumption',
                     'Consumption (import) & production (export)': 'consumption_production',
                     'Macromolecule degradation': 'macromolecule_degradation',
                     'Production (export)': 'production'}

# Make a dictionary linking node ID to node label
for node in xroot:
    if node.tag == '{http://www.cs.rpi.edu/XGMML}node':
        node_dict[node.attrib.get("id")] = node.attrib.get("label")

# Make for each microbe-metabolite interaction, a dictionary containing source, target and interaction
for node in xroot:
    if node.tag == '{http://www.cs.rpi.edu/XGMML}edge':
        children = list(node)
        interaction = None
        for child in children:
            if child.attrib.get("name") == 'interaction':
                interaction = child.attrib.get("value")
        edge_rows.append({"source": node_dict[node.attrib.get("target")],
                          "target": node_dict[node.attrib.get("source")],
                          "interaction": interaction_names[interaction]})

</pre></code>

There is one peculiarity we need to deal with: the <code>include_nodes</code> function that we are going to use, does not add metadata for nodes that do not currently exist in the database. Therefore, we will first run a custom query that creates all source nodes as <code>Microbe</code> nodes. This is also necessary because not all metabolite consumers / producers in the microbe/metabolite are actually microbes; colonocytes, for example, will not show up in our association network derived from metabarcoding data. 

We first start the driver and run a batch query to address this. The <code>edge_rows</code> list is already in a format that can be used for these queries. The driver will return all names of the nodes it created, we can simply ignore those. Next, we will add the remainder of the list of dictionaries using the <code>include_nodes</code> function. This function uses the <code>name</code> and <code>label</code> parameters to identify node labels, while the <code>nodes</code> parameter should be a list of dictionaries containing source and target nodes. 


<pre><code>
driver = IoDriver(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=loc,
                  encrypted=False)
                  
query = "WITH $batch as batch " \
        "UNWIND batch as record " \
        "MERGE (a:Microbe {name:record.source}) RETURN a"
driver.write(query, batch=edge_rows)
driver.include_nodes(nodes=edge_rows, name="Metabolite", label="Microbe")
</pre></code>

Now that the entire literature network has been uploaded to Neo4j, we can start querying this network through Neo4j (Figure 1). 

<figure>
  <img src="/images/literature_network.PNG" alt="Screenshot of Neo4j Browser showing Sung et al. literature network." width="600"> 
  <figcaption>Figure 1: Screenshot of Neo4j Browser showing Sung et al. literature network.</figcaption>
</figure>

However, there is one major issue we need to solve: the Sung et al. network has complete species identifiers, but our association network does not. Therefore, we will parse the Sung et al. nodes to connect them to <code>Genus</code> identifiers; since nearly all of our association networks do have those connections, we should be able to link our association network to metabolites that way. We can similarly use the <code>include_nodes</code> function to connect our nodes. 

<pre><code>
genus_dict = []
for edge in edge_rows:
    microbe = edge['source']
    genus_dict.append({'source': microbe,
                       'target': 'g__' + microbe.split(' ')[0]})
driver.include_nodes(nodes=genus_dict, name="Genus", label="Microbe")
</pre></code>

Our association network nodes are stored as <code>Taxon</code> nodes. Can we link these nodes to the literature network now (Figure 2)? Indeed, it looks like we should be able to identify associations that could be linked to specific metabolites. 

<figure>
  <img src="/images/literature_associations.PNG" alt="Screenshot of Neo4j Browser showing Sung et al. literature nodes connecting to association network." width="600"> 
  <figcaption>Figure 2: Screenshot of Neo4j Browser showing Sung et al. literature nodes connecting to association network.</figcaption>
</figure>
