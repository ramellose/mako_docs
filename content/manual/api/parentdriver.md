---
title: "ParentDriver"
description: ""
lead: ""
date: 2021-04-28T16:34:14+02:00
lastmod: 2021-04-28T16:34:14+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 3
toc: true
---

The ParentDriver class provides some general class methods available to all other mako drivers. 

<div style="outline:0.01em solid black; padding:10px;">
<b><code>ParentDriver.close()</code></b>

Closes the connection to the database. 

</div>
<br>

<div style="outline:0.01em solid black; padding:10px;">
<b><code>ParentDriver.query(query, batch=None)</code></b><br>
<b><code>ParentDriver.write(query, batch=None)</code></b>

Accepts a query (read or write) and provides the results. 
For batch queries, the batch parameter should contain a list of dictionaries, where each dictionary contains a key: value pair where the key matches a key in the Cypher query.

Batch queries should unwind the batch, like so:
<pre><code>
query = "WITH $batch as batch " \
"UNWIND batch as record " \
"MERGE (a:Taxon {name:record.taxon}) RETURN a"
</pre></code>

The string after record (here taxon) needs to match a dictionary key.

<ul>
  <li><b>query:</b> String containing Cypher query</li>
  <li><b>batch:</b> List of dictionaries for batch queries</li>
</ul>
</div>