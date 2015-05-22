#!/usr/bin/python

class Session(object):

	def __init__(self, session):
		self.new = session['new']
		self.sessionId = session['sessionId']
		self.attributes = session['attributes']
		self.user = session['user']

	def getUserId(self):
		return self.user['userId']

	def getAttributeNames(self):
		return list(attributes.keys())