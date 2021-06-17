---
title: "Using the API"
description: ""
lead: ""
date: 2021-04-20T11:36:28+02:00
lastmod: 2021-04-20T11:36:28+02:00
draft: false
images: []
menu: 
  manual:
    parent: "API"
weight: 200
toc: true
---

To use the API in Python scripts, you need a Python interpreter. You can run a Python interpreter through an IDE (integrated development environment) like <a href="https://www.spyder-ide.org/">Spyder</a> or <a href="https://www.jetbrains.com/pycharm/">PyCharm</a>. 

You can also start a Python interpreter by running <code>python</code>. If you installed mako via conda, make sure to start the Python interpreter from conda so the interpreter can find the mako package. The screenshot below shows how the interpreter can be started from conda. After the interpreter has started, you can copy Python code shown on the webpage and run this line by line. 

<figure>
  <img src="/images/interpreter.PNG" alt="Command prompt showing how a conda environment is used to start a Python interpreter and import mako in that interpreter." width="600"> 
  <figcaption>Figure 1: Command prompt showing how a conda environment is used to start a Python interpreter and import mako in that interpreter.</figcaption>
</figure>

Most of the Python code used in the case studies is also provided as a separate script. Assuming that you have a conda environment called <code>myenv</code> that contains mako, you can run the scripts from that environment. For example, to run a script called <a href="https://ramellose.github.io/mako_docs/demo/custom_queries.py">custom_queries.py</a>, run the following code:

<pre><code>
conda activate myenv
python custom_queries.py
</code></pre>

