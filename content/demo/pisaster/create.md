---
title: "Creating the food web"
description: ""
lead: ""
date: 2021-04-21T09:54:37+02:00
lastmod: 2021-04-21T09:54:37+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Pisaster"
weight: 5
toc: true
---

After connecting to the Neo4j database, the textbox at the top of the Neo4j Browser can be used to type Cypher queries and interact with the database. Click the blue triangle next to the textbox to run a query. A Cypher query contains several clauses, <code>MERGE</code> being one of them. Each clause tells the DBMS what to do. In this case, the clauses tell the DBMS to unwind the list and match or create a node. Those nodes are then returned. 
For convenience, we will unwind a list of organism names (<code>WITH [], UNWIND</code>) and then use the <code>MERGE</code> query in combination with the unwound values to create all organisms. If an organism already exists, the <code>MERGE</code> query is equivalent to a <code>MATCH</code> query, meaning it just finds the node. 

<pre><code>
WITH ['Pisaster', 'Thais sp.', 'Chitons', 'Limpets', 
'Bivalves', 'Acorn barnacles', 'Mitella'] as organisms
UNWIND organisms as x WITH x
MERGE (a:Organism {name: x}) RETURN a
</code></pre>

The Neo4j Browser will automatically highlight the structure of the query (Figure 4). Additionally, the query returns all created nodes. You should see the created nodes as disconnected, floating circles in the browser. 

<figure>
  <img src="/images/organismquery.PNG" alt="Neo4j Browser query." width="600"> 
  <figcaption>Figure 4: Neo4j Browser query.</figcaption>
</figure>

Next, we create the relationships between the nodes. Because this is slightly more complicated and includes setting relationship properties, we will run a separate query for each relationship. Each query first finds the two organisms (<code>MATCH</code>) and then creates the relationship with number and calories values (<code>MERGE</code>). Again, these are returned if successful.  

{{< alert icon="👉" text="The queries below need to be run one by one. " >}}

<pre><code>
MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Chitons'}) MERGE (a)-[r:PREYS_ON {number: 0.03, calories: 0.41}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Limpets'}) MERGE (a)-[r:PREYS_ON {number: 0.05, calories: 0.05}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Bivalves'}) MERGE (a)-[r:PREYS_ON {number: 0.27, calories: 0.37}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Thais sp.'}) MERGE (a)-[r:PREYS_ON {number: ' x', calories: 0.02}]-(b) RETURN a, b   

MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Acorn barnacles'}) MERGE (a)-[r:PREYS_ON {number: 0.63, calories: 0.12}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Pisaster'}), (b:Organism {name: 'Mitella'}) MERGE (a)-[r:PREYS_ON {number: 0.01, calories: 0.03}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Thais sp.'}), (b:Organism {name: 'Bivalves'}) MERGE (a)-[r:PREYS_ON {number: 0.05, calories: 0.10}]-(b) RETURN a, b

MATCH (a:Organism {name: 'Thais sp.'}), (b:Organism {name: 'Acorn barnacles'}) MERGE (a)-[r:PREYS_ON {number: 0.95, calories: 0.90}]-(b) RETURN a, b
</code></pre>