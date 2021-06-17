---
title: "Github"
description: ""
lead: ""
date: 2021-05-11T14:39:01+02:00
lastmod: 2021-05-11T14:39:01+02:00
draft: false
images: []
menu: 
  installation:
    parent: "Installation"
weight: 3
toc: true
---

The latest version of mako can be downloaded from the Github page: <a href="https://github.com/ramellose/mako">https://github.com/ramellose/mako</a>.

To install mako from Github, you can use <code>pip</code>:<br>

<code>python3 -m pip install git+https://github.com/ramellose/mako.git</code>

Note that mako has several dependencies that may need to be installed separately. Specifically, you need to have installed <code>biom-format</code>, a package required for reading BIOM files. If you have trouble installing these dependencies, please install mako using conda. 

After installation, you should be able to call mako:
<pre><code>
mako -h
</pre></code>