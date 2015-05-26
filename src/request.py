#!/usr/bin/python


class Request(object):

    def __init__(self, requestId):
        self.requestId = requestId


class LaunchRequest(Request):

    def __init__(self, requestId):

        super(LaunchRequest, self).__init__(requestId)


class IntentRequest(Request):

    def __init__(self, requestId, intent):
        self.name = intent['name']
        self.slots = intent['slots']

        super(IntentRequest, self).__init__(requestId)


class SessionEndRequest(Request):

    def __init__(self, requestId, reason):
        self.reason = reason

        super(SessionEndRequest, self).__init__(requestId)
