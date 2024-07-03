import requests
import json


# Custom Library imports:
from .files import read_file
from .errors import *

class Ks_http:
	def __init__(self, x_auth_token: str):
		self.headers = {'X-Auth-Token': x_auth_token}



	@staticmethod
	def __handle_api_errors(response_text: str) -> None:
		if '"httpResponseCode":200' not in response_text:
			raise KsApiError(response_text)



	def post_scan(self, url: str, data: dict, files=None) -> str:
		with requests.post(url,
			headers=self.headers,
			files=files,
			data=data
		) as response:
			self.__handle_api_errors(response.text)
			return json.loads(response.text)



	def get_req(self, url: str) -> dict:
		with requests.get(url,
			headers=self.headers,
		) as response:
			self.__handle_api_errors(response.text)
			return response.text



	def get_req_json(self, url: str) -> dict:
		with requests.get(url,
			headers=self.headers,
		) as response:
			self.__handle_api_errors(response.text)
			return json.loads(response.text)


