#!/usr/bin/python
import Request

class SessionEndRequest(Request):

	def __init__(self, requestId, reason):
		self.reason = reason

		super(IntentRequest, self).__init__(requestId)