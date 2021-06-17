---
title: "Setting up the database"
description: ""
lead: ""
date: 2021-04-28T13:57:31+02:00
lastmod: 2021-04-28T13:57:31+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Custom queries"
weight: 202
toc: true
---
Find all Python code used on this page here: <a href="https://ramellose.github.io/mako_docs/demo/custom_setup.py">custom_setup.py</a><br>

Before we can write any queries, the database needs to be populated first. We will use the BIOM and graphml files from the Code Ocean capsule here. You can replace these with any other BIOM or graphml file of your choice, like the demo data in <a href="../vignette/intro">the vignette</a>. 

First, we load all software packages and collect all the file paths of the files we want to write to the database. For instructions on starting a Python interpreter, please see the <a href="https://ramellose.github.io/mako_docs/manual/api/python/">API section of the manual</a>. 
<pre><code>
import biom
import networkx as nx
import os
from mako.scripts.neo4biom import Biom2Neo
from mako.scripts.io import IoDriver

filepath = "C:/Users/username/demo/"

biom_filepaths = [filepath + "11766.biom", 
                  filepath + "11888.biom", 
                  filepath + "11947.biom",
                  filepath + "12021.biom",
                  filepath + "12716.biom"]
                  
network_filepaths = [filepath + "11766.graphml", 
                     filepath + "11888.graphml", 
                     filepath + "11947.graphml",
                     filepath + "12021.graphml",
                     filepath + "12716.graphml"]
</pre></code>

We will add the BIOM files first, so the next section imports the <code>Biom2Neo</code> driver, connects to the Neo4j database and then loops over the file paths to read the BIOM files and write them to the database. In this case, we are assuming that you are running Neo4j from the Docker container (<a href="../../neo4j/docker/docker/">link to Docker setup</a>), so we will use these connection settings. We use the filenames to set the experiment ID in the database. 

<pre><code>
driver = Biom2Neo(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=filepath,
                  encrypted=False)

for file in biom_filepaths:
    name = os.path.basename(file)
    name = name.split(".")[0]
    biomtab = biom.load_table(file)
    driver.convert_biom(biomfile=biomtab, exp_id=name, obs=True)
driver.close()
</pre></code>

With the BIOM files uploaded, we can do the same thing for the network files, now using the <code>IoDriver</code> class. 
<pre><code>
driver = IoDriver(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=filepath,
                  encrypted=False)

for file in network_filepaths:
    name = os.path.basename(file)
    name = name.split(".")[0]
    net = nx.read_graphml(file)
    driver.convert_networkx(network=net, network_id=name)
driver.close()
</pre></code>

That's it! Now that there is a populated Neo4j database, we can start running our own queries. 