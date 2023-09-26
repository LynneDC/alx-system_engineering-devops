<h1>WEB SERVER</h1>
<h2>Resources</h2>
<p>
<ul>
   <em>
      <li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works">HOW WEB WORKS</a>.</li>
      <li><a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04">HOW TO CONFIGURE NGINX</a>.</li>
      <li><a href="https://landingi.com/help/domains-vs-subdomains/">ROOT AND SUB DOMAIN</a>.</li>
    </em>
<h3>Requirements</h3>
<p>
<ul>
  <li>Allowed editors: vi, vim, emacs</li>
  <li>All your files will be interpreted on Ubuntu 16.04 LTS and checked with Shellcheck</li>
  <li>First line of all your Bash scripts should be <b>#!/usr/bin/env bash</b></li>  
<hr />
<h4>TASKS : MANDATORY</h4>

<p><b>0. Transfer a file to your server</b></p>
  <li>Write a Bash script that transfers a file from our client to a server<li>

<p><b>1. Install nginx web server</b></p>
<ol>
  <li>Install nginx on server listening on port 80</li>
</ol>
<p><b>2. Setup a domain name</b></p>
<ol>
  <li>provide the domain name only and configure your DNS records with an A entry </li>
</ol>

<p><b>3. Redirection</b></p>

<ol>
  <li>Readme:
    <ul>
      <li>Configure your Nginx server so that /redirect_me is redirecting to another pagee</li>
      <li>Write Bash script containing commands to automatically configure a Ubuntu machine</li>
      <li><a href="https://stackoverflow.com/questions/26041088/sed-replace-line-with-multiline-variable">Replace a line with multiple lines with sed</a>.</li>
    </ul>
  </li>
<p><b>4. Not found page 404</b></p>
  <li>Configure your Nginx server to have a custom 404 page that contains a string
    <ul>
      <li>The page must return an HTTP 404 error code</li>
      <li>configure a brand new Ubuntu machine</li>
    </ul>
  </li>
</ol>
<h5>TASKS: ADVANCED<h5>
<p>5. Install Nginx web server (w/ Puppet)</p>
<li>install and configure an Nginx server using Puppet instead of Bash include resources in your manifest to perform a 301 redirect when querying /redirect_me.
    <ul>
      <li>Nginx should be listening on port 80</li>
      <li>The redirection must be a “301 Moved Permanently”</li>
    </ul>
  </li>
</ol>

<p>If text is indented, it is treated as a block quotation, and the final attribution line is handled automatically:</p>
<blockquote>
Should array indices start at 0 or 1?
My suggested compromise of 0.5 was rejected without, I thought, proper consideration.
-- Stan Kelly-Bootle</blockquote>

<p>reST uses :: prior to a pre-formatted code block:</p>
<pre class="literal-block">
Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
</pre>

<p>Multi-line text can<br/>span in tables<br/>with a pipe character.</p>I
