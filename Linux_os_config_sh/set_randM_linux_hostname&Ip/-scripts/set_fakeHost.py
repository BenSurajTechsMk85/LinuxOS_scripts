import random
import string
import os

def rand_string(length):
    rand_str = "".join(random.choice(string.ascii_lowercase
    +string.ascii_uppercase
    +string.digits) for i in range(length))

    return rand_str

def rand_int(n1,n2):

    rand_ranage_nos = random.randrange(n1,n2)

    return rand_ranage_nos


def get_host_id():
    
    randm_str_v = rand_string(8)

    randm_int_v = rand_int(10,1000)

    id = f'{randm_str_v}-{randm_int_v}'

    return id


def set_hostname(hostname):

        lnx_set_hostname_cmd = f'hostnamectl set-hostname {hostname}'

        os.system(lnx_set_hostname_cmd)

        print(f"\n- host name changed to '{hostname}'")

def set_hosts_fl(host_id):

        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

        wrds = [f'{ip}       localhost\n',f'{ip}   {host_id}.kali        {host_id}']


        with open("/etc/hosts",'w+') as wfl:
                wfl.writelines(wrds)
        
        print(f"\n- '/etc/hosts' config changed -> ip: {ip} , hostname: {host_id}")

def main():

        returned_host_id = get_host_id()

        set_hostname(returned_host_id)

        set_hosts_fl(host_id=returned_host_id)


if __name__=='__main__':
        main()

