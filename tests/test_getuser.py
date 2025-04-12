import uuid

import pytest

from conftest import load_user_data
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
	return APIS()


def test_getUser_validation(apis):
	responses=apis.get('users')
	print(responses.json())
	assert  responses.status_code==200
	assert  len(responses.json()) > 0

def test_createUser_validation(apis,load_user_data):
	# user_data = {
	# 	"name": "rani shetty",
	# 	"username": "qa1 member",
	# 	"email": "rani@gmail.com"
	# }
	user_data = load_user_data["new_user"]
	unique_email= f"{uuid.uuid4().hex[:8]}@gmail.com"
	print(unique_email)
	user_data["email"] = unique_email
	responses=apis.post('users',user_data)
	print(responses.json())
	assert  responses.status_code==201
	assert  responses.json()['name'] == 'rani shetty'
	# check the get also
	id = str(responses.json()['id'])
	getResponses=apis.get('users/10')
	print(responses.json())
	assert  getResponses.status_code==200
	assert  getResponses.json()['name']=='Clementina DuBuque'

def test_updateUser_validation(apis):
		user_data = {
			"name": "roll",
			'username': 'roll_qa',
			'email': 'roll@233.biz'
		}
		updateResponses = apis.put('users/1', user_data)
		print(updateResponses.json())
		assert updateResponses.status_code == 200
		assert updateResponses.json()['name'] == 'roll'


def test_deleteUser_validation(apis):
	responses = apis.delete('users/1')
	print(responses.json())
	assert responses.status_code == 200
	assert responses.json() == {}, "no data"



