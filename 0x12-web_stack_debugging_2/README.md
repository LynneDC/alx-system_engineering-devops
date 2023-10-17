<h1>Web stack debugging #2</h1>
<h2> DESCRIPTION </h2>
  <P> Web server debugging where you change web port to port 0:80. By changing the contents of sites enabled to be the same as site available. That happens in default file of site-available and enabled folder in server</p>
 <h2>Resources</h2>
<p>
<ul>
   <li><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/287/99littlebugsinthecode-holberton.jpg" alt="that little bug" /></li>
   <li><a href="https://intranet.alxswe.com/concepts/68">Web Stack Debugging</a>.</li>
</ul>
<h2>Requirements</h2>
</p>
<ul>
  <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
  <li>All your files should end with a new line</li>
  <li>A README.md file at the root of the folder of the project is mandatory</li>
  <li>All your Bash script files must be executable</li>
  <li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
  <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>
<h2>TASKS : MANDATORY</h2>
<p><b>0. Run software as another user</b></p>
<ol><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231017%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231017T063004Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dd9e3bf3e70e328c4e2c955abb752b9c6399549d381285a60cbf5d3212ba20df"alt="ROOT" />
   <ul>
   <li>Write a Bash script accepts one argument</li>
   <li>the script should run the whoami command under the user passed as an argument</li>
   <li>make sure to try your script by passing different users</li>
   </ul>
</ol>
<p><b>1. Run Nginx as Nginx</b></p>
<ol>
  <li>Fix this container so that Nginx is running as the nginx user.<li>
  <h3> Requirements:</h3>
   <li>nginx must be running as nginx user</li>
   <li>nginx must be listening on all active IPs on port 8080</li>
   <li>You cannot use apt-get remove</li>
   <li>Write a Bash script that configures the container to fit the above requirements</li>

<h2>TASKS: ADVANCED<h5>
<p><b>2. 7 lines or less</b></p>
<ol>
   <h3>Requirements:</h3>
    <ul>
      <li>Using what you did for task #1, make your fix short and sweet.</li>
       <li>Your Bash script must be 7 lines long or less</li>
       <li>You cannot use ;, &&, wget</li>
       <li>You cannot execute your previous answer file </li>
     </ul>
</ol>
<pre class="literal-block">
</pre>
<p><br/><br/></p>
