#!/usr/bin/python


class Response(object):

    def __init__(self, response):
        self.outputSpeech = response['outputSpeech']
        self.shouldEndSession = response['shouldEndSession']


class OutputSpeech(object):

    def __init__(self, speechType, text):
        self.speechType = speechType
        self.text = text


class Card(object):

    def __init__(self, cardType, title, subtitle, content):
        self.cardType = cardType
        self.title = title
        self.subtitle = subtitle
        self.content = content
