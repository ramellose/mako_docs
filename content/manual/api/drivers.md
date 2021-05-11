---
title: "Using a driver class"
description: ""
lead: ""
date: 2021-04-20T11:36:34+02:00
lastmod: 2021-04-20T11:36:34+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 202
toc: true
---

While mako's functions can be called from command line, they have also been documented extensively so they can be used from a Python script. The <code>base</code>, <code>neo4biom</code>, <code>io</code>, <code>netstats</code>, <code>metastats</code> and <code>utils</code> modules each contain a class that can interact with a running Neo4j database instance. To carry out the functions as part of a script, simply instantiate an object with the necessary information to connect to the database and it will set up a Neo4j driver that can be used to run mako-specific functions or to run custom queries. 

All Neo4j driver classes in mako inherit methods from the <code>ParentDriver</code> class and therefore have a query method that can be used to run Cypher queries. Queries can be passed as a string. If appliccable, dictionaries for parameterized batch queries can also be used. 

For example, the <code>io</code> module contains the <code>IoDriver</code> class. The <code>IoDriver</code>, like other mako drivers, can be called by providing Neo4j access details:

<pre>
<code>
from mako.scripts.io import IoDriver
driver = IoDriver(user="testuser", 
                  password="test",
                  uri=inputs['address'], 
                  filepath="C:/testfolder/",
                  encrypted=False)
driver.convert_networkx(network=networkx_object, network_id="test_network"
</code>
</pre>
 
