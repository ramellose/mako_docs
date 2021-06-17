---
title: "Database schema for mako"
description: ""
lead: ""
date: 2021-04-21T16:29:49+02:00
lastmod: 2021-04-21T16:29:49+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Schema"
weight: 302
toc: true
---

The database schema used by mako was designed to meet several demands:
<ul>
    <li>Simple querying of BIOM data</li>
    <li>Simple querying of network data</li>
    <li>Respect hierarchical structure of taxonomic tree</li>
    <li>Straightforward access of networks for meta-analyses</li>
    <li>Flexible inclusion of metadata</li>
</ul>

The complete schema, sufficient to import BIOM files and network files, therefore specifies both standard node types and node relationships (Figure 1). 

<div id="labeldata", style="height:150px; border:3px solid black; padding:10px">
<span id="labelspan"> <a href="https://www.ebi.ac.uk/ols/ontologies/ncit">Find the complete NCI Thesaurus here.</a> Zoom and drag to move the schema and click the nodes to see their NCIt definitions. </span></div>

<div id="mynetwork", style="height:500px"></div>

<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<script>
  // create an array with nodes
  var nodes = new vis.DataSet([
    { id: 1, label: "Edge", title: 'NCIT:C75923'},
    { id: 2, label: "Experiment", title: 'NCIT:C42790'},
    { id: 3, label: "Network", title: 'NCIT:C61377'},
    { id: 4, label: "Property", title: 'NCIT:C20189'},
    { id: 5, label: "Specimen", title: 'NCIT:C19157'},
    { id: 6, label: "Taxon", title: 'NCIT:C40098'},
    { id: 7, label: "Species", title: 'NCIT:C45293'},
    { id: 8, label: "Genus", title: 'NCIT:C45292'},
    { id: 9, label: "Family", title: 'NCIT:C45290'},
    { id: 10, label: "Order", title: 'NCIT:C45287'},
    { id: 11, label: "Class", title: 'NCIT:C45280'},
    { id: 12, label: "Phylum", title: 'NCIT:C45277'},
    { id: 13, label: "Kingdom", title: 'NCIT:C45276'},
   ]);

  // create an array with edges
  var edges = new vis.DataSet([
    { from: 1, to: 3, label: 'part_of'},
    { from: 5, to: 2, label: 'part_of' },
    { from: 6, to: 5, label: 'located_in'},
    { from: 6, to: 1, label: 'participates_in'},
    { from: 4, to: 5, label: 'quality_of'},
    { from: 4, to: 6, label: 'quality_of'},
    { from: 6, to: 7, label: 'member_of'},
    { from: 6, to: 8, label: 'member_of'},
    { from: 6, to: 9, label: 'member_of'},
    { from: 6, to: 10, label: 'member_of'},
    { from: 6, to: 11, label: 'member_of'},
    { from: 6, to: 12, label: 'member_of'},
    { from: 6, to: 13, label: 'member_of'},
    { from: 7, to: 8, label: 'member_of'},
    { from: 8, to: 9, label: 'member_of'},
    { from: 9, to: 10, label: 'member_of'},
    { from: 10, to: 11, label: 'member_of'},
    { from: 11, to: 12, label: 'member_of'},
    { from: 12, to: 13, label: 'member_of'},
  ]);

  // create a network
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {};
  var network = new vis.Network(container, data, options);
  
  network.on("click", function (params) {
    var dict = { 
              1: "A connection between nodes in a graph.",
              2: "A coordinated set of actions and observations designed to generate data, with the ultimate goal of discovery or hypothesis testing.",
              3: "An interconnected system of things or people.",
              4: "A distinguishing quality or prominent aspect of a person, object, action, process, or substance.", 
              5: "A part of a thing, or of several things, taken to demonstrate or to determine the character of the whole, e.g. a substance, or portion of material obtained for use in testing, examination, or study; particularly, a preparation of tissue or bodily fluid taken for examination or diagnosis.",
              6: "Ranked categories for the classification of organisms according to their suspected evolutionary relationships.", 
              7: "A group of organisms that differ from all other groups of organisms and that are capable of breeding and producing fertile offspring.",
              8: "A taxonomic category ranking below a family (or Subfamily) and above a species and generally consisting of a group of species exhibiting similar characteristics.", 
              9: "A taxonomic category between Order and Genus. It consists of a group of organisms among which the differences are quite minor, e.g. Equiidae - horses and their relatives.", 
              10: "A taxonomic category between Class and Family. It is group of organisms that although differing quite a bit among themselves still have a large degree of characteristics in common.", 
              11: "A collection of taxonomic subdivisions directly under Phylum. It is a major group of organisms, e.g. Mammalia, Reptilia, Gastropoda, Insecta, etc that contains a large number of different sublineages, but have shared characteristics in common (e.g. warm-blooded, fur, six legs etc).", 
              12: "A major division of a biological kingdom, consisting of closely-related classes; represents a basic fundamental pattern of organization and, presumably, a common descent.", 
              13: "The highest taxonomic rank, immediately above phylum or division. There are five biological kingdoms (Monera, Protista, Plantae, Fungi, Animalia) into which organisms are grouped, based on common characteristics."};
    // your element, edge or node
    console.log(params);
    var currentID = params.nodes[0];
    if (typeof(currentID) == "undefined") {
      // find edges
      var currentID = params.edges[0];
      var newLabel = edges.get(currentID).label
    } else {
      var newLabel = dict[currentID];
    }
    // set span text
    document.getElementById("labelspan").innerHTML = newLabel;
});
</script>
Figure 1: mako OWL schema. 