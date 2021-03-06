
from sys import argv
import os
import subprocess
from bashyAPI import *



targ = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/assets/"



first_command = argv[1]
pckg_name = argv[2]
api_name = argv[4]

#install package flow
def install_package(api: str, pckg_name : str, targ : str) -> str:
	git_url = get_package_url(pckg_name, api)
	subprocess.call(["(cd {};  git clone {}; cd ..; cd src; echo source {} >> bashy_aliases )".format(targ, git_url, targ + pckg_name + "/" + pckg_name +".sh")], shell = True)

	#"git clone {}".format(git_url)
	#subprocess.call(["git clone {}".format(git_url)], shell = True)

#update package flow
def update_package(api : str, pckg_name : str, targ : str) -> str:
	git_url = get_package_url(pckg_name, api)
	subprocess.call(["cd {}; cd {}; git pull".format(targ,pckg_name)], shell = True)

if first_command in ["install", "update"]:
	PROFILEURL = r'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tq='.format(os.getenv("PROFILEURL"))
	target_api = r'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tq='.format(get_api_url(PROFILEURL, api_name))

	if first_command == "install":
		install_package(target_api, pckg_name, targ)
	elif first_command == "update":
		update_package(target_api, pckg_name, targ)

