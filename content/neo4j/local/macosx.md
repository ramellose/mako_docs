---
title: "macOS"
description: ""
lead: ""
date: 2021-04-20T16:25:37+02:00
lastmod: 2021-04-20T16:25:37+02:00
draft: false
images: []
menu: 
  neo4j:
    parent: "Local"
weight: 3
toc: true
---

While you can run Neo4j as a console application, you can also run it as a service. However, you need to create the service manually using <a href="https://www.launchd.info/">launchd</a>. You can find all instructions for running Neo4j as a macOS service in the <a href="https://neo4j.com/docs/operations-manual/current/installation/osx/#_macos_service">macOS section of the Operations Manual</a>. The instructions below are to run the console application on macOS computers. 

<ul>
    <li>Download the macOS version of Neo4j listed under Community server</li>
    <li>Unzip the Neo4j download in a folder of your choice</li>
    <li>In command line, navigate to the Neo4j folder where you unzipped the download</li>
    <li>Run <code>./bin/neo4j console</code> to start the server</li>
    <li>Run <code>CTRL+C</code> to stop the server</li>
</ul>
