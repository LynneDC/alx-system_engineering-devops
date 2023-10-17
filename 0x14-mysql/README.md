<!DOCTYPE html>
<html>
<head>
<h1>
 MySQL
</h1>
</head>
<body style="font-family: Verdana, Arial, sans-serif">
   <h2> DESCRIPTION </h2>
   <p>
      Database management and manipulation. :
   <li><a href="https://intranet.alxswe.com/concepts/100002"> DATABASE ADMIN</a></li>
   <li><a href="https://intranet.alxswe.com/concepts/68"> Web Stack Debigging</a></li>
   <li><a href="https://intranet.alxswe.com/concepts/100002">How To Install mysql</a></li> 
  </p>
 
   <h2 style="color: green; round-color:RED ">
        Background Context
   </h2>
   <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png" alt="FULLSTACKE FOR LIFE " />

   <h2>RESOURCES</h2>
   <ol>
   <ul>
   <li><a href="https://intranet.alxswe.com/rltoken/eojqG9FZbA6QVWN5P9cLzA" >What is a primary-replica cluster</a></li>
   <li><a href="https://intranet.alxswe.com/rltoken/z2KVk2UKLMc0RvHMdJmYLg"> Mysql primary replica setup</a></li>
   <li><a href="https://intranet.alxswe.com/rltoken/BharnxaLb-BDDYFywzME2Q">Build A Robust Database Backup Strategy</a></li>


   <h2 style="color: #FF645F; margin-left: 40px">
     Requirements
   </h2>
   <ol>
   <li>Allowed editors: vi, vim, emacs</li>
   <li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
   <li> The second line of all your Bash scripts should be a comment </li>
   <li>README.md file, at the root of the folder of the project</li>
   </ol>

   <h2 style="color: #FF645F; margin-left: 40px">
	     Tasks: MANDATORY
	</h2>
  <h2 style="color: white; background-color:#61b3e7">
	     0. Install MySQL
  </h2>
  <p> 
   First things first, let’s get MySQL installed on both your web-01 and web-02 servers.
   <h4> Requirements: </h4>
   <ol>
   <li>MySQL distribution must be 5.7.x</li>
   <li>Please make sure you have your README.md pushed to GitHub.</li>
  </ol>
  </p>
  <h3 style="color: #FF645F; margin-left: 40px">
         1. Let us in!
  </h3>
  <p>
     create a user and password for both MySQL databases 
   <h4>REQUIREMENTS:</h4>
   <ul>
   <li> Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn.</li>
   <li> holberton_user has permission to check the primary/replica status of your databases.</li>
   <li> Add the public key to web-02 as you only added it to web-01 for this project</li>
   </ul>
   <h3 style="color: #FF645F; margin-left: 40px">
         2. If only you could see what I've seen with your eyes
  </h3>
  <p>  
   Create a database named tyrell_corp.
  <h4> Requirements: </h4>
  <li> Within the tyrell_corp database create a table named nexus6 and add at least one entry to it</li>
  <li>Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty. </li>
   </P>
 <h3> 3. Quite an experience to live in fear, isn't it? </h3>
 <p> On your primary MySQL server (web-01), create a new user for the replica server. </p>
 <h4> REQUIREMENTS </h4>
 <ol>
   <ul>
   <li>The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like</li>
   <li>replica_user must have the appropriate permissions to replicate your primary MySQL server.</li>
   <li>holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.</li>
  </ul>
  </ol>
 <h3>4. Setup a Primary-Replica infrastructure using MySQL</h3>

<h3> 5. MySQL backup </h3>

 </body>
</html>
