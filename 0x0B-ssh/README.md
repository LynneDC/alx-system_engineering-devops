
```html
<!DOCTYPE html>
<html>

<head>
    <title>0x0B. SSH DevOps Project</title>
</head>

<body>

    <h1>0x0B. SSH DevOps Project</h1>

    <h2>Background Context</h2>

    <p>
        Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like
        level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect
        using a password but an RSA key. We’ve configured your server with the public key you created in the first task
        of a previous project shared in your intranet profile.
    </p>

    <p>
        You can access your server information in the my servers section of the intranet, each line with contains the IP
        and username you should use to connect via ssh.
    </p>

    <p><strong>Note:</strong> Your server is configured with an Ubuntu 20.04 LTS environment.</p>

    <h2>Resources</h2>

    <p>Read or watch:</p>

    <ul>
        <li><a href="#">What is a (physical) server - text</a></li>
        <li><a href="#">What is a (physical) server - video</a></li>
        <li><a href="#">SSH essentials</a></li>
        <li><a href="#">SSH Config File</a></li>
        <li><a href="#">Public Key Authentication for SSH</a></li>
        <li><a href="#">How Secure Shell Works</a></li>
        <li><a href="#">SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still
                confusing. It may be helpful to watch at x1.25 speed or above.)</a></li>
    </ul>

    <p>For reference:</p>

    <ul>
        <li><a href="#">Understanding the SSH Encryption and Connection Process</a></li>
        <li><a href="#">Secure Shell Wiki</a></li>
        <li><a href="#">IETF RFC 4251 (Description of the SSH Protocol)</a></li>
        <li><a href="#">Internet Engineering Task Force</a></li>
        <li><a href="#">Request for Comments</a></li>
    </ul>

    <p>man or help:</p>

    <ul>
        <li><a href="#">ssh</a></li>
        <li><a href="#">ssh-keygen</a></li>
        <li><a href="#">env</a></li>
    </ul>

    <h2>Learning Objectives</h2>

    <p>
        At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
    </p>

    <ul>
        <li>What is a server</li>
        <li>Where servers usually live</li>
        <li>What is SSH</li>
        <li>How to create an SSH RSA key pair</li>
        <li>How to connect to a remote host using an SSH RSA key pair</li>
        <li>The advantage of using #!/usr/bin/env bash instead of /bin/bash</li>
    </ul>

    <h2>Requirements</h2>

    <h3>General</h3>

    <ul>
        <li>Allowed editors: vi, vim, emacs</li>
        <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
        <li>All your files should end with a new line</li>
        <li>A README.md file, at the root of the folder of the project, is mandatory</li>
        <li>All your Bash script files must be executable</li>
        <li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
    </ul>

    <h3>Your servers</h3>

    <table>
        <tr>
            <th>Name</th>
            <th>Username</th>
            <th>IP</th>
            <th>State</th>
        </tr>
        <tr>
            <td>251885-web-01</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <!-- Add more server information as needed -->
    </table>

    <h2>Tasks</h2>

    <h3>0. Use a private key (mandatory)</h3>

    <p>
        Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user
        ubuntu.
    </p>

    <p><strong>Requirements:</strong></p>

    <ul>
        <li>Only use ssh single-character flags</li>
        <li>You cannot use -l</li>
        <li>You do not need to handle the case of a private key protected by a passphrase</li>
    </ul>

    <p><strong>Example:</strong></p>

    <code>sylvain@ubuntu$ ./0-use_a_private_key</code>

    <!-- Repeat the above structure for other tasks -->

</body>

</html>
```
