<!DOCTYPE html>
<html lang="en">
  <head>
  <h1>Project: 0x15. API</h1>
</head>
<body>
<p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>

<p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them &ndash; access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>

<p>This is a perfect example of a task that is not suited for Bash scripting, so let&rsquo;s build Python scripts.</p>

<h2>RESOURCES</h2>
<p><strong>READ or WATCH</strong>:</p>
<ul>
<li><a href="/rltoken/KMFzqRAqedMf7AHHBD_43g" title="Friends don&#39;t let friends program in shell script" target="_blank">Friends don&rsquo;t let friends program in shell script</a> </li>
<li><a href="/rltoken/zeBO6_RNTlwaotyRRNAzoQ" title="What is an API" target="_blank">What is an API</a> </li>
<li><a href="/rltoken/bf09Qp6QY44CANLzxxRbPA" title="What is an API? In English, please" target="_blank">What is an API? In English, please</a></li>
<li><a href="/rltoken/fA164QWEnZxaSngBD3EPRQ" title="What is a REST API" target="_blank">What is a REST API</a> </li>
<li><a href="/rltoken/n4h77IbBuDxTE3bhes_AyQ" title="What are microservices" target="_blank">What are microservices</a> </li>
<li><a href="/rltoken/b7V1ROY6kSRxDDKnsJoqxg" title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" target="_blank">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a> </li>
</ul>
<h2>KNOWLEDE TEST </h2>
<ul>
<li>What Bash scripting should not be used for</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>

<h2> REQUIREMENTS </h2>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.* .* </code>) </li>

<li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use <a href="/rltoken/CNqOWPW6mdYuK7Ak-f2KHQ" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
<li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;:</code>)</li>
</ul>

<h2 class="gap">TASKS MANDATORY</h2>
<h3 class="panel-title">
      0. Gather data from an API
</h3>
 <p>Write a Python script that, using this <a href="/rltoken/7cr7aLYdaWAZWBKrBKS12A" title="REST API" target="_blank">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p>
<h4>Requirements:</h4>

<ul>
<li>You must use <code>urllib</code> or <code>requests</code> module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:

<ul>
<li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>

<ul>
<li><code>EMPLOYEE_NAME</code>: name of the employee</li>
<li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
<li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: <code>TASK_TITLE</code> (with 1 tabulation and 1 space before the <code>TASK_TITLE</code>)</li>
</ul></li>
</ul>
<h3 class="panel-title">
      1. Export to CSV
</h3>
<p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p>

<h4>Requirements:</h4>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li>
<li>File name must be: <code>USER_ID.csv</code></li>
</ul>

<h3 class="panel-title">
      2. Export to JSON
</h3>
<p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<h4>Requirements:</h4>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [{&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, ... ]}</code></li>
<li>File name must be: <code>USER_ID.json</code></li>
</ul>

 <h3 class="panel-title">
      3. Dictionary of list of dictionaries
</h3>
 <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<h4>Requirements:</h4>

<ul>
<li>Records all tasks from all employees</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li>
<li>File name must be: <code>todo_all_employees.json</code></li>
</ul>

</body>
</html>


