'''
test.py act as a 3rd party software..(like android / ios)
'''

import json
import requests
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

# def get_response(id=None):
# 	data = {}
# 	if id is not None:
# 		data = {
# 			'id': id,
# 		}
	
# 	response = requests.get(BASE_URL + ENDPOINT, data = json.dumps(data))
# 	print('='*100)
# 	print(response.status_code)
# 	print(response.json())
# 	print('='*100)
# get_response(1)

# def get_all():
# 	response = requests.get(BASE_URL + ENDPOINT2)
# 	print(response.status_code)
# 	print(response.json())
# # get_all()


# def create_resource():
# 	dict_data = {
# 		'eno':600,
# 		'ename':'kalu',
#     	'esal':'4001',
#     	'eaddr':'bangalore',
# 	}
# 	response = requests.post(BASE_URL + ENDPOINT, data = json.dumps(dict_data))
# 	print('*'*100)
# 	print(response.status_code)
# 	print(response.json())
# 	print('*'*100)
# create_resource()


# def update_resource(id):
# 	new_emp = {
# 		'id':id,
# 		'esal':'9999',
# 		'ename':'Makar',
# 	}
# 	response = requests.put(BASE_URL + ENDPOINT, data = json.dumps(new_emp))
# 	print('*'*100)
# 	print(response.status_code)
# 	print(response.json())
# 	print('*'*100)
# update_resource(100)

def delete_resource(id):
	data = {
		'id':id,
	}
	response = requests.delete(BASE_URL + ENDPOINT, data = json.dumps(data))
	print('*'*100)
	print(response.status_code)
	print(response.json())
	print('*'*100)
delete_resource(6)



