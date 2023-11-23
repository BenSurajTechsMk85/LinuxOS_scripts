#!/bin/bash

# Linux OS , change file persmission (r = read, w = write , x = execute) only for current user:
# chmod 700 docker_install_auto-debian.sh

sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker -y

sudo systemctl enable docker

sudo systemctl start docker

sudo systemctl status docker