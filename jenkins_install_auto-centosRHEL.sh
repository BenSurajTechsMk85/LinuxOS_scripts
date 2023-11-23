#!/bin/bash

# Linux OS , change file persmission (r = read, w = write , x = execute) only for current user:
# chmod 700 jenkins_install_auto-centosRHEL.sh
# result: ls -> rwx------- jenkins_install_auto-centosRHEL.sh

# Required only when installing fresh linux os or as AWS Ec2 instance
# sudo yum update -y

sudo yum update -y

sudo wget -o /etc/yum.repos.dd/jenkins.repo https://[kkg.jenkins.io/redhat-stable/jenkins.repo

sudo rpm --import https://pkg.jenkins.io./redhat-stable/jenkins.io-2023

sudo yum upgrade

sudo install java-11-amazon-coretto -y

suod yum install jenkins -y

sudo systemctl enable jenkins

sudo systemctl start jenkins

# sudo systemctl status jenkins

# Change security group inbound rule with port number 8080 and TCP ip access as anywhere (0.0.0.0/0)