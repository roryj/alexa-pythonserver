#!/usr/bin/python
from src.response import Response
import json


class AlexaResponse(object):

    def __init__(self, sessionAttributes, outputSpeech, card, shouldEndSession):
        self.version = "1.0"
        self.sessionAttributes = sessionAttributes
        self.response = Response(outputSpeech, card, shouldEndSession)

    def __str__(self):
        return "{\"version\": \"" + self.version + "\", " + "\"sessionAttributes\": " + json.dumps(self.sessionAttributes) + "\", " + "\"response\": " + str(self.response) + "}"