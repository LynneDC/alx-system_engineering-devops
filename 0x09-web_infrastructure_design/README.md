# Web Infrastructure Design Project

## Introduction

This repository contains the solutions and diagrams for the Web Infrastructure Design project as part of the DevOps and SysAdmin track. The project focuses on designing and explaining different levels of web infrastructures, from a simple setup to a more complex, secured, and monitored one.

## Table of Contents

- [Task 0: Simple Web Stack](#task-0-simple-web-stack)
- [Task 1: Distributed Web Infrastructure](#task-1-distributed-web-infrastructure)
- [Task 2: Secured and Monitored Web Infrastructure](#task-2-secured-and-monitored-web-infrastructure)

## Task 0: Simple Web Stack

In this task, we designed a basic web infrastructure composed of a single server with a LAMP stack. The key components include:
- 1 Server
- 1 Web Server (Nginx)
- 1 Application Server
- 1 Application Files (Code Base)
- 1 Database (MySQL)
- Domain name foobar.com configured with a www record pointing to server IP 8.8.8.8

### Explanation

- What is a server?
- Role of the domain name
- DNS record type for www in www.foobar.com
- Role of the web server
- Role of the application server
- Role of the database
- Communication between the server and user's computer

### Issues

- Single Point of Failure (SPOF)
- Downtime during maintenance
- Limited scalability for high traffic

## Task 1: Distributed Web Infrastructure

In this task, we expanded the infrastructure to a three-server setup, introducing load balancing and database replication. The components added are:
- 2 Servers
- 1 Web Server (Nginx)
- 1 Application Server
- 1 Load Balancer (HAproxy)
- 1 Application Files (Code Base)
- 1 Database (MySQL Primary-Replica Cluster)

### Explanation

- Reasons for adding each element
- Load balancer distribution algorithm and setup
- Active-Active vs. Active-Passive setup
- Primary-Replica database cluster operation
- Differences between Primary and Replica nodes

### Issues

- Single Points of Failure
- Security vulnerabilities
- Lack of monitoring

## Task 2: Secured and Monitored Web Infrastructure

In this task, we enhanced the infrastructure's security and monitoring aspects. We added:
- 3 Firewalls
- SSL certificate for HTTPS
- 3 Monitoring clients (Sumologic or other services)

### Explanation

- Purpose of each additional element
- Use of firewalls
- Importance of serving traffic over HTTPS
- Role of monitoring and data collection
- Monitoring web server QPS

### Issues

- SSL termination at load balancer level
- Single MySQL server for writes
- Homogeneous components across servers

## Conclusion

This project demonstrates the design considerations and trade-offs involved in building web infrastructures of varying complexities. Each task focused on specific aspects of infrastructure design, scalability, security, and monitoring.

For detailed diagrams and screenshots, please refer to the respective task directories.

**Note:** This README provides an overview. For detailed diagrams and explanations, refer to individual task files in this repository.

**Project Team:**  
- Roseline Dangazela <roselinedc1308@gmail.com>
- Donpaul Oduor 
