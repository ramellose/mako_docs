---
title: "Querying the food web"
description: ""
lead: ""
date: 2021-04-21T09:54:49+02:00
lastmod: 2021-04-21T09:54:49+02:00
draft: false
images: []
menu: 
  demo:
    parent: "Pisaster"
weight: 6
toc: true
---

To get the complete network, we can run the query below. Notice the LIMIT statement; when we have networks with thousands of nodes, it is crucial to limit the number of returned items to prevent the Neo4j Browser from crashing. In this case, the LIMIT is higher than the total number of items, so we simply get the complete network. 

<code>
MATCH (n) RETURN n LIMIT 50
</code>

You should get a graph in the Neo4j Browser that contains the entire food web. When you mouse over the relationships, you can see the values; when you drag and drop nodes, you can even rearrange the entire network so it looks like Figure 1! You can see an example of the Neo4j network below (Figure 5). 

<figure>
  <img src="/images/pisasterneo4j.PNG" alt="Neo4j Browser query output." width="600"> 
  <figcaption>Figure 5: Neo4j Browser query output.</figcaption>
</figure>

Since the relationships are directed, there is not even truly a need to specify that some species are predators and others are prey. We can simply use the directionality to find species that interact in a certain direction. The first of these queries returns all predators, the second returns all prey! Finally, the third query filters on the relationships so that only prey are returned that make up over 20% of a predator's calories. 

<code>MATCH (a)-->(b) RETURN a </code>
<code>MATCH (a)-->(b) RETURN b </code>
<code>MATCH (a)-[r]->(b) WHERE r.calories > 0.20 RETURN b LIMIT 50 </code>

Explaining the full potential of Cypher is not within the scope of this short guide. Note that many other clauses have not been addressed here, such as CREATE. For a complete overview of Cypher, we refer to the <a href="https://neo4j.com/docs/cypher-manual/current/">Neo4j manual</a>. For explanations of the mako data schema and related queries, please visit <a href="https://ramellose.github.io/mako_docs/cypher/introduction/intro/"the Cypher page of this website.</a> 
