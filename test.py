'''
test.py act as a 3rd party software..(like android / ios)
'''

import json
import requests
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/4/"
ENDPOINT2 = "api/"

def get_response():
    response = requests.get(BASE_URL + ENDPOINT)
    print(response.status_code)
    print(response.json())
# get_response()

def get_all():
	response = requests.get(BASE_URL + ENDPOINT2)
	print(response.status_code)
	print(response.json())
# get_all()


def create_resource():
	dict_data = {
		'eno':500,
		'ename':'Ringa',
    	'esal':'5001',
    	'eaddr':'Barabazar',
	}
	response = requests.post(BASE_URL + ENDPOINT2, data = json.dumps(dict_data))
	print('*'*100)
	print(response.status_code)
	print(response.json())
	print('*'*100)
# create_resource()