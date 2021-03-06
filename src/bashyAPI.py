import requests
from urllib.parse import urlencode
import json

def get_api_url(user_api : str, target_api : str)  -> str:
	query="select%20B%20where%20A%20='{}'".format(target_api)
	print(user_api, query)
	response = requests.get(user_api + query)
	result = json.loads(response.text[47:-2])
	return result['table']['rows'][0]['c'][0]['v']
	

def get_package_url(pckg_name: str, api : str) -> str:
	query = "select%20C%20where%20B%20='{}'".format(pckg_name)
	response = requests.get(api + query)
	result = json.loads(response.text[47:-2])
	return result['table']['rows'][0]['c'][0]['v']


