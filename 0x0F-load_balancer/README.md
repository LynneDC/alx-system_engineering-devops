<H1>Load balancer</h1>
<h2> DESCRIPTION </h2>
  <P> Let's make our systme more robust and reliable by adding new servers and a load balancer to redirect and share traffic equally</p>
 <ol>
   <ul>
     <li>CONCEPTS</li>
     <li><a href="https://intranet.alxswe.com/concepts/46">Load balancer</a>.</li>
     <li><a href="https://intranet.alxswe.com/concepts/68"> Web stack debugging</a>.</li>
  <ul>
<ol>
 
<h2>Resources</h2>
<p>
<ul>
   <li><a href="https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ">Introduction to Load Balancer</a>.</li>
   <li><a href="https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw">HTTP header</a>.</li>
   <li><a href="https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg">Debian/Ubuntu HAProxy packages</a>.</li>
</ul>
<h2>Requirements</h2>
</p>
<ul>
  <li>Allowed editors: vi, vim, emacs</li>
  <li>All your files will be interpreted on Ubuntu 20.04 LTS and checked with shellcheck</li>
  <li>First line of all your Bash scripts should be <b>#!/usr/bin/env bash</b></li>
</ul>
<h2>TASKS : MANDATORY</h2>
<p><b>0. Double the number of webservers</b></p>
<ol>
   <ul>
      <li>Configure Nginx so that its HTTP response contains a custom header </li>
      <li>The name of the custom HTTP header must be X-Served-By</li></li>
      <li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</a>.</li>
      <li>Write 0-custom_http_response_header so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
      <li><a href="https://intranet.alxswe.com/rltoken/k3Bt6zu1On_-mDszxi0Z9w">Ignore SC2154 for shellcheck</a>.</li>
   </ul>
</ol>

<p><b>1. Install your load balancer</b></p>

<ol>
   <ul>
      <li>Install and configure HAproxy on your lb-01 server.</li>
      <li>Distribute requests using a roundrobin algorithm</li>
      <li>write a Bash script that configures a new Ubuntu machine </li>
      <li>Make sure that HAproxy can be managed via an init script</li>
      <li>Configure HAproxy so that it send traffic to web-01 and web-02</li>
   </ul>
</ol>
<h2>TASKS: ADVANCED<h5>
<p><b>2. Add a custom HTTP header with Puppet</b></p>
<ol>
    <ul>
      <li>automate the task of creating a custom HTTP header response,</li>
       <li>The name of the custom HTTP header must be X-Served-By</li>
       <li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
       <li>Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
     </ul>
</ol>
<pre class="literal-block">
</pre>
<p><br/><br/></p>
