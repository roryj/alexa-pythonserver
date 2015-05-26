#!/usr/bin/python
from src.respone import Response


class AlexaResponse(object):

    def __init__(self, shouldEndSession):
        self.version = "1.0"
        self.shouldEndSession = shouldEndSession
        self.outputSpeech = {}
        self.card = {}


    def setOutputSpeech(self, speechType = "PlainText", text):
        self.outputSpeech.type = speechType
        self.outputSpeech.text = text


    def setCard(self, cardType = "Simple", title, subtitle, content):
        self.card.type = cardType
        self.card.title = title
        self.card.subtitle = subtitle
        self.card.content = content


    def __str__(self):
        return 
