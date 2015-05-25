#!/usr/bin/python

class AlexaRequest(object):

	def __init__(self, alexaRequest):
		self.version = alexaRequest['version']
		self.sessionAttributes = alexaRequest['sessionAttributes']

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