import requests


class APIS:
	BASE_URL = "https://jsonplaceholder.typicode.com"

	def __init__(self):
		self.header ={
			"Content-Type" : "application/json"}

	def get(self,endpoint):
		url=f'{self.BASE_URL}/{endpoint}'
		responses=requests.get(url, headers=self.header)
		return responses


	def post(self,endpoint,data):
		url=f'{self.BASE_URL}/{endpoint}'
		responses=requests.post(url, headers=self.header, json=data)
		return responses

	def put(self,endpoint,data):
		url=f'{self.BASE_URL}/{endpoint}'
		responses=requests.put(url, headers=self.header, json=data)
		return responses
	def delete(self,endpoint):
		url=f'{self.BASE_URL}/{endpoint}'
		responses=requests.delete(url, headers=self.header)
		return responses