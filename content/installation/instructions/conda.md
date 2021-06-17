---
title: "Conda"
description: ""
lead: ""
date: 2021-05-11T14:39:07+02:00
lastmod: 2021-05-11T14:39:07+02:00
draft: false
images: []
menu: 
  installation:
    parent: "Installation"
weight: 2
toc: true
---

Conda environments including mako can be installed from the conda page: <a href="https://anaconda.org/ramellose/mako">https://anaconda.org/ramellose/mako</a>. 

To create a new environment including mako, the channel hosting mako, as well as the bioconda channels, need to be added first:
<pre><code>
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --add channels ramellose
</code></pre>

The environment can then be created using conda:
<pre><code>
conda create -n myenv mako 
conda activate myenv
</pre></code>

After installation, you should be able to call mako:
<pre><code>
mako -h
</pre></code>