#!/bin/bash

# Linux OS , change file persmission (r = read, w = write , x = execute) only for current user:
# chmod 700 docker_install_auto-centosRHEL.sh
# result: ls -> rwx------- docker_install_auto-centosRHEL.sh

# Required only when installing fresh linux os or as AWS Ec2 instance
# sudo yum update -y

sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker -y

sudo systemctl enable docker

sudo systemctl start docker

# sudo systemctl status docker