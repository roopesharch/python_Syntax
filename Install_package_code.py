import sys
import subprocess
class install_packages:
    def __init__(self):
        #list the package needed to install in a python list
        package_list=['selenium','pandas','time','bs4']
        for i in package_list:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
            except Exception as e:
                print("\n?????\n", e,"\n?????")

install_packages()      

# call the code from another python file using below code
# from package_installer import *
