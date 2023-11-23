import pkgutil
import os
import sys


def pip_install_requirements():

        pkgs = ['Faker']

        for pkg in pkgs:

                if pkgutil.find_loader!=None:

                        print(f"\n- '{pkg}' python package\\module is installed or already exists\n -")

                else:

                        print(f"\n- '{pkg}' python package\\module is not installed \n -")

                        pip_install_pkg_cmd = os.system(f"python -m pip install {pkg}")

                        print(pip_install_pkg_cmd)

def fakeip():

        from faker import Faker
        from faker.providers import internet

        faker = Faker()

        faker_ip_pub  = faker.ipv4(internet)

        return faker_ip_pub

def set_net_ip(net):

        returned_fakeip = fakeip()

        lnx_set_ip_cmd = f'ifconfig {net} {returned_fakeip}'

        os.system(lnx_set_ip_cmd)

        print(f"\n {net} ip changed to '{returned_fakeip}'")


def main():

        try:

                pip_install_requirements()

                opts = sys.argv[1]

                if '-n' in opts:

                        net_in = sys.argv[2]

                        set_net_ip(net_in)

                else: 

                        print('\n - Option invalid')

        except IndexError as indexerr:


                print(f"\n-ArgERR!! Parametres\\Arguments are insuffcient , cause: \n {indexerr}")

        except Exception as err:

                print(f"\n-GenERR!! Generic error , cause: \n {err}")
        

if __name__=='__main__':
        main()
