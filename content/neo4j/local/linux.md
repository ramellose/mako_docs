---
title: "Linux"
description: ""
lead: ""
date: 2021-04-20T16:25:19+02:00
lastmod: 2021-04-20T16:25:19+02:00
draft: false
images: []
menu: 
  neo4j:
    parent: "Local"
weight: 2
toc: true
---

You can find all instructions for running Neo4j as a Linux service in the <a href="https://neo4j.com/docs/operations-manual/current/installation/linux/systemd/#linux-service">Linux section of the Operations Manual</a>.
To run Neo4j on Linux, you need to first install the RPM package. Instructions for installations of the RPM package can also be found in the <a href="https://neo4j.com/docs/operations-manual/current/installation/linux/rpm/">Linux section of the Operations Manual</a>. After installation of RPM (and possibly rebooting your system), you can follow the instructions below to start the service on Linux computers. 

<ul>
    <li>Run <code>systemctl start neo4j</code> to start the service</li>
    <li>Run <code>systemctl stop neo4j</code> to stop the service</li>
</ul>
