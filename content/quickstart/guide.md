---
title: "Quickstart"
description: ""
date: 2021-05-10T15:40:25+02:00
lastmod: 2021-05-10T15:40:25+02:00
draft: false
images: []
---

<h3>Prerequisites</h3>
Please make sure you have <a href="https://docs.docker.com/get-docker/">Docker</a> and <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/">Conda</a> installed. 
<h3>Set up a Neo4j database</h3>
<video controls="" height="200" width="500">
<source src="/videos/docker.mp4" type="video/mp4"> </source>
</video>
<a href="/neo4j/docker/docker">For additional information, <br>see the instructions on <b>Setting up Docker</b>.</a>
<h3>Connect with Neo4j Browser</h3>
<video controls="" height="300" width="500">
<source src="/videos/browser.mp4" type="video/mp4"> </source>
</video><br>
The username and password for the browser are "neo4j" and <br>"test" respectively. <br><a href="/neo4j/browser/browser">Find additional instructions on <b>Neo4j Browser</b> here.</a>
<h3>Install mako through Conda</h3>
Follow the instructions on the installation page: <a href="/installation/instructions/conda/">mako installation</a>. 
<h3>Write data to the Neo4j database</h3>
<a href="/examples/sponges/intro">Please follow this link to download files for the <b>Sponges</b> case study.</a> <br>In your command-line interface, navigate to the location where <br>you downloaded and unzipped the files (the sponge_biomfiles <b>and</b> the sponge_networks zip files). <br><br>
Commands:<br>
<code>mako neo4biom -u neo4j -p test -a neo4j://localhost:7688 -cf -biom sponge_biomfiles</code><br>
<code>mako io -cf -net sponge_networks</code>

<video controls="" height="200" width="500">
<source src="/videos/mako.mp4" type="video/mp4"> </source>
</video><br>
<h3>Find microbial associations of interest</h3>
<video controls="" height="300" width="500">
<source src="/videos/query.mp4" type="video/mp4"> </source>
</video><br>
Query: <code>MATCH p=(:Order {name: 'o__Nitrospirales'})--(:Taxon)<br>--(:Edge)--(:Taxon)--(:Order {name: 'o__Cenarchaeales'}) <br>RETURN p LIMIT 25 </code><br>
<a href="/cypher/introduction/intro">Visit the Cypher webpages for additional instructions on working with <b>Cypher</b>.</a>
