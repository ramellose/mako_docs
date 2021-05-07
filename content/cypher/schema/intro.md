---
title: "Schemas for associations"
description: ""
lead: ""
date: 2021-04-21T16:29:54+02:00
lastmod: 2021-04-21T16:29:54+02:00
draft: false
images: []
menu: 
  cypher:
    parent: "Schema"
weight: 1
toc: true
---

Database schemas are blueprints that describe how data in a database is organized. By defining schemas, we are able to design queries that can access data stored according to those schemas. Hence, mako's core component is a database schema constructed from several OWL terms. This database schema also defines constraints for the data and provides guidance on how data needs to be uploaded to become easily accessible. Most functionality of the API uses the schema to rapidly upload BIOM files, check edge weights or find associations between related species. 

To properly integrate with Neo4j's ability to work with ontology web language (OWL), each node and relationship label is derived from an existing ontology, the NCI Thesaurus (Sioutos et al., 2007). However, since relationships are not well-defined across biological ontologies, constraints for relationships were defined manually with Protégé (Noy et al., 2001). For each relationship, domains and ranges (target and source nodes) were specified. While these axioms are not added to Neo4j as actual constraints, mako can run checks to see if domain and range axioms are violated by any nodes or relationships in the database. 

In this chapter, the database schema used by mako is described in detail to aid in the design of custom queries that can carry out additional tasks on Neo4j databases. 

Noy, N. F., Sintek, M., Decker, S., Crubézy, M., Fergerson, R. W., & Musen, M. A. (2001). Creating semantic web contents with protege-2000. <i>IEEE intelligent systems, 16</i>(2), 60-71.

Sioutos, N., de Coronado, S., Haber, M. W., Hartel, F. W., Shaiu, W. L., & Wright, L. W. (2007). NCI Thesaurus: a semantic model integrating cancer-related clinical and molecular information. <i>Journal of biomedical informatics, 40</i>(1), 30-43.