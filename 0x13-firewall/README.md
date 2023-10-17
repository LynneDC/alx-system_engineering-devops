<!DOCTYPE html>
<html>
<head>
<h1>
 FIREWALL
</h1>
</head>
<body style="font-family: Verdana, Arial, sans-serif">
   <h2> DESCRIPTION </h2>
   <p>
      Protecting your data from internet attack is a priority. Firewall to the rescue:
   </p>
   <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" alt="FIREWALL" />
   <h2 style="color: green; round-color:RED ">
        Background Context
   </h2>
   <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" alt="Server without firewall " />

   <h2> Resources </h2>
   <li><a href="https://intranet.alxswe.com/rltoken/vjB4LyHRdtEImzZcuD89ZQ">What Is Firewall</a>
  
   <h2 style="color: #FF645F; margin-left: 40px">
     Requirements
   </h2>
   <ol>
      <li>README.md file, at the root of the folder of the project</li>
   </ol>

   <h2 style="color: #FF645F; margin-left: 40px">
	     Tasks: MANDATORY
	</h2>
  <h2 style="color: white; background-color:#61b3e7">
	     0. Block all incoming traffic but.
  </h2>
  <p> 
   Let’s install the ufw firewall and setup a few rules on web-01.
   <h4> Requirements: </h4>
   <ol>
   <li>Configure ufw so that it blocks all incoming traffic, except the following TCP ports</li>
   <ul>
   <li>22 (SSH) </li>
   <li> 443 (HTTPS SSL)</li>
   <li>	80 (HTTP)</li>
   </ul>
   <li>	Share the ufw commands that you used in your answer file</li>
  
  </ol>
  </p>
   <h2> TASK: ADVANCED </h2>

  <h3 style="color: #FF645F; margin-left: 40px">
         1. Port forwarding
  </h3>
  <p>  
     Firewalls can not only filter requests, they can also forward them.
  <h4> Requirements: </h4>
  <li> Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP</li>
  <li> Your answer file should be a copy of the ufw configuration file that you modified to make this happen </li>
   </P>
 </body>
</html>
