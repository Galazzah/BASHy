from sys import argv
import os
import subprocess
from bashyAPI import *


URL = r'https://docs.google.com/spreadsheets/d/14pMZ-SvxD1ui5UZMs82TjH_ykDsVo713uY7mbyw5Rm0/gviz/tq?tq='
targ = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/assets/"

first_command = argv[1]
pckg_name = argv[2]


#install package flow
def install_package(api: str, pckg_name : str, targ : str) -> str:
	git_url = get_package_url(pckg_name, api)
	subprocess.call(["(cd {};  git clone {}; cd ..; cd src; echo source {} >> bashy_aliases )".format(targ, git_url, targ + pckg_name + "/" + pckg_name +".sh")], shell = True)

	#"git clone {}".format(git_url)
	#subprocess.call(["git clone {}".format(git_url)], shell = True)

#update package flow
def update_package(api : str, pckg_name : str, targ : str) -> str:
	git_url = get_package_url(pckg_name, api)
	subprocess.call(["cd {}; git pull {}".format(targ, git_url)], shell = True)


if first_command == "install":
	install_package(URL, pckg_name, targ)
elif first_command == "update":
	#update
	update_package(URL, pckg_name, targ)

	
