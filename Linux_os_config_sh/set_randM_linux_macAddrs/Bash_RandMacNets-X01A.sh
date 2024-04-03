#/bin/bash
lst_nets_cmd="ls /sys/class/net/"
nets=$(eval "$lst_nets_cmd")
for net in $nets;
do
   echo $net
   macchanger -r $net
   echo "\n!- Net: $net | MacAddrs Changed -!\n"
done
