#!/bin/bash
# change shell file permission to root user only access:
# sudo chmod 700 start_fakeip.sh 

python -u /etc/udev/set_fakeIp.py -n eth0

python -u /etc/udev/set_fakeHost.py

systemctl restart NetworkManager
                                        