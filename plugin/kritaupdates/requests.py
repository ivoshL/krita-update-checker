import urllib.request
import urllib.parse

# http classes to make using the local server's API easier
###################################################################
class Response():
	def __init__(self, response):
		self.__response = response
		self.ok = 300 > self.__response.code >= 200
		try:
			self.content = response.read().decode('utf-8')
		except:
			self.content = ''

	def __str__(self):
		return '<Response ['+str(self.__response.code)+']>'

class requests():
	@staticmethod
	def get(url):
		return Response(urllib.request.urlopen(url))
###################################################################
