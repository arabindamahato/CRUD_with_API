'''
test.py act as a 3rd party software..(like android / ios)
'''


import requests
BASE_UR = "http://127.0.0.1:8000/"
ENDPOINT = "api/4/"
def get_response():
    response = requests.get(BASE_UR + ENDPOINT)
    print(response.json())
    print(response.status_code)
get_response()
