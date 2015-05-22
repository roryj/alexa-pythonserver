#!/usr/bin/python
import Request

class IntentRequest(Request):

	def __init__(self, requestId, intent):
		self.name = intent['name']
		self.slots = intent['slots']

		super(IntentRequest, self).__init__(requestId)