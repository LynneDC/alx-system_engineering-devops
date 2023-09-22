<center><h1>Configuration management</h1></center>

This repository contains the initial stage of a student project configuration management in devops.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/LynneDC/alx-system_engineering-devops/0x0A-configuration_management/blob/dev/AUTHORS) | Project authors |
| 1: puppet-lint | N/A | All code is puppet-lint compliant|
| 2: Create a file | [0-create_a_file.pp](https://github.com/LynneDC/alx-system_engineering-devops/0x0A-configuration_management/blob/dev/[0-create_a_file.pp) | create a file in /tmp. that is not empt and has read, write and execute permisions |
| 4.Install a package | [1-install_a_package.pp](https://github.com/LynneDC/alx-system_engineering-devops/0x0A-configuration_management/blob/dev/[1-install_a_package.pp]) | installs  flask from pip3 using puppet|
| Execute a command | [2-execute_a_command.pp](https://github.com/LynneDC/alx-system_engineering-devops/0x0A-configuration_management/blob/dev/[2-execute_a_command.pp]) | Executes a command using exec and pkill|
<br>
<br>
<center> <h2>General Use</h2> </center>

#### INSTALLATION
	* to install puppet
	```
	$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
  	$ apt-get install -y ruby-augeas
	$ apt-get install -y ruby-shadow
	$ apt-get install -y puppet
	```
	* to install puppet-lint
	```
	$ gem install puppet-lint
	```

<br>
<br>
<br>
