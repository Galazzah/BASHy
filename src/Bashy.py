from sys import argv
import os
import subprocess
from bashyAPI import *


URL = r'https://sheetsu.com/apis/7c526569'
targ = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/assets/"
print(targ)
first_command = argv[1]
pckg_name = argv[2]


#install package flow
def install_package(api: str, pckg_name : str, targ : str) -> str:
	response = get_response(URL)
	pckg = get_package(response, pckg_name)
	git_url = get_package_url(pckg)
	subprocess.call(["(cd {};  git clone {})".format(targ, git_url)], shell = True)

	#"git clone {}".format(git_url)
	#subprocess.call(["git clone {}".format(git_url)], shell = True)
install_package(URL, pckg_name, targ) 
	