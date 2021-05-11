---
title: "Functions"
description: ""
lead: ""
date: 2021-04-29T13:43:31+02:00
lastmod: 2021-04-29T13:43:31+02:00
draft: false
images: []
menu: 
  examples:
    parent: "Motifs"
weight: 502
toc: true
---

To process Cypher query results, we first need to be able to handle some peculiarities of query behaviour. As addressed in <a href="../../../demo/query/custom">the Custom Queries demo</a>, some patterns can be matched in reverse. Take for example the 3-node clique consisting of nodes A, B and C. The pattern can match this as A--B--C--A, but also as B--C--A--B or C--A--B--C. All three options will be returned as results. Consequently, we first need to write a function that returns only the unique nods. 

In pseudo-code, the function does the following:
<pre><code>
1. For query result p, make a new list of lists with only dictionaries in each sublist (nodes are dictionaries)
2. If there is query result q (and r), extend the list of lists with dictionaries in those query results
3. Sort every sublist
4. Filter each sublist so only unique nodes are present
5. Only return unique sublists
</pre></code>

See the Python implementation below. 

<pre><code>
def get_unique_patterns(query_result):
    """
    Sorts all node names,
    then returns a set of tuples with only unique node names.
    :param query_result: Neo4j query outcome (list of dictionaries)
    :return:
    """
    all_motifs = [[y['name'] for y in x['p'] if type(y) == dict] for x in query_result]
    if 'q' in query_result[0]:
        for i in range(len(all_motifs)):
            all_motifs[i].extend([y['name'] for y in query_result[i]['q'] if type(y) == dict])
            all_motifs[i].extend([y['name'] for y in query_result[i]['r'] if type(y) == dict])
    for y in all_motifs:
        y.sort()
    # the duplicated first node is variable,
    # need to use set() to filter this
    # otherwise each pattern with
    # a different duplicate node is recognized as unique
    all_motifs = [set(x) for x in all_motifs]
    all_motifs = set(map(tuple, all_motifs))
    return all_motifs
</pre></code>

Secondly, we want to investigate the EMPO_2 annotations of each motif, so we can state if a motif occurred in an Animal, Plant, Non-saline or Saline network. To do so, we will use a function that takes a reference dictionary linking taxa to specific studies. 

In pseudo-code, the function does the following:
<pre><code>
1. Run the query
2. If the query collects edges ('j' query output):
    1. Get unique edge identifiers
    2. For each edge, get the matching taxa
    3. For each EMPO_2 term, check if taxa are in that specific EMPO_2 list
    4. Assign that EMPO_2 association to the edge
3. If the query collects motifs ('p' query output):
    1. Get the unique motifs
    3. For each EMPO_2 term, check if a node in a motif is in that specific EMPO_2 list
    4. Assign that EMPO_2 term to the motif
4. Take the given results dictionary and add the new counts
5. Return the results dictionary
</pre></code>

See the Python implementation below. 

<pre><code>
def count_motifs_empo(query, driver, tax_dict, count_dict, i):
    """
    Takes a query, the driver and two dictionaries,
    outputs number of unique query results per EMPO assignment
    :param query:
    :param driver:
    :param tax_dict: dictionary with taxa belonging to an EMPO_2 annotation
    :param count_dict: dictionary with e
    :param i: key for count_dict that is currently applicable
    :return:
    """
    motifs = driver.query(query)
    # this means the motif only contains edges
    if len(motifs) == 0:
        return count_dict
    if 'j' in motifs[0]:
        unique_edges = dict.fromkeys([x['j']['name'] for x in motifs])
        for motif in motifs:
            edge = motif['j']['name']
            taxon = motif['i']['name']
            for empo in tax_dict:
                if taxon in tax_dict[empo]:
                    unique_edges[edge] = empo
        for edge in unique_edges:
            count_dict[unique_edges[edge]][i] += 1
    if 'p' in motifs[0]:
        motifs = get_unique_patterns(motifs)
        for link in motifs:
            for empo in tax_dict:
                match = [x for x in link if x in tax_dict[empo]]
                if len(match) > 0:
                    count_dict[empo][i] += 1
    return count_dict
</pre></code>

Together, these functions are sufficient to get the number of unique motifs per EMPO_2 annotation. 
