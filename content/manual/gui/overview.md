---
title: "GUI Overview"
description: ""
lead: ""
date: 2021-04-20T11:35:20+02:00
lastmod: 2021-04-20T11:35:20+02:00
draft: false
images: []
menu: 
  manual:
    parent: "GUI"
weight: 301
toc: true
---

The GUI provides a graphical interface for most of the functionality of the CLI (Figure 2). The GUI interface largely follows the same structure as the CLI, meaning most CLI parameters are shown in the GUI and have a tooltip explaining the parameter choice.

<figure>
  <img src="/images/gui.PNG" alt="Graphical user interface for mako." width="600"> 
  <figcaption>Figure 2: Graphical user interface for mako.</figcaption>
</figure>

There are two ways to run the GUI: via executable or by installing mako and its dependencies locally. 
You can download the executables from the <a href="https://github.com/ramellose/mako/releases">the mako releases page</a>. Releases that come with updated executables have them listed in the release description. Currently, executables are only available for Windows and Linux systems. 

Alternatively, the the <code>main_GUI.py</code> script can be run directly to start the GUI. On Mac systems, this requires the mako package and all its dependencies to be installed to the local Python version. You may therefore have to download multiple dependencies manually. All dependencies can be found here: <a href="https://github.com/ramellose/mako/blob/master/meta.yaml">mako meta.yaml file with dependencies</a>. 

To run the GUI, clone the repository to a local folder, navigate to the folder containing the mako scripts and run the script that starts the GUI. 
<pre><code>
git clone https://github.com/ramellose/mako.git
cd mako/mako
python main_GUI.py
</pre></code>

To install mako's dependencies, you can use the following commands for packages available through PyPi:
<pre><code>
python -m pip install neo4j
</pre></code>

Some packages may only be available through Github. In that case, you can install them as follows: 
<pre><code>
python -m pip install git+https://github.com/ramellose/manta.git
</pre></code>


