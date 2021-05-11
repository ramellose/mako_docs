---
title: "BaseDriver"
description: ""
lead: ""
date: 2021-04-28T16:34:30+02:00
lastmod: 2021-04-28T16:34:30+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 204
toc: true
---

The BaseDriver class clears the database and checks constraints. 

<div style="outline:0.01em solid black; padding:10px;">
<b><code>BaseDriver.clear_database()</code></b>

Clears the database, deleting all nodes and edges. 

</div>
<br>
<div style="outline:0.01em solid black; padding:10px;">
<b><code>BaseDriver.check_domain_range()</code></b>

This function uses the Neo4j driver and the ontology to check whether there are properties in the database that violate the domains and ranges specified in the ontology.
</div>
<br>
<div style="outline:0.01em solid black; padding:10px;">
<b><code>BaseDriver.add_constraints()</code></b>

This function adds some constraints for unique node names specified in the data schema. 

</div>