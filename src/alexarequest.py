#!/usr/bin/python
from src.session import Session
from src.request import LaunchRequest, SessionEndRequest, IntentRequest

class AlexaRequest(object):

	def __init__(self, alexaRequest):
		self.version = alexaRequest['version']
		self.session = Session(alexaRequest['session'])

		request = alexaRequest['request']

		requestType = request['type']

		if requestType == 'LaunchRequest':
			self.request = LaunchRequest(request['requestId'])
		elif requestType == 'IntentRequest':
			self.request = IntentRequest(request['requestId'], request['intent'])
		elif requestType == 'SessionEndRequest':
			self.request = SessionEndRequest(request['requestId'], request['reason'])
		else:
			self.request = {}