#!/usr/bin/python


class Response(object):

    def __init__(self, outputSpeech, card, shouldEndSession):
        self.outputSpeech = outputSpeech
        self.card = card
        self.shouldEndSession = shouldEndSession
        
    def __str__(self):
        return "{\"outputSpeech\": " + str(self.outputSpeech) + ", \"card\": " + str(self.card) + ", \"shouldEndSession\": " + str(self.shouldEndSession) + "}"


class OutputSpeech(object):

    def __init__(self, text, speechType='PlainText'):
        self.speechType = speechType
        self.text = text
        
    def __str__(self):
        return "{\"type\": \"" + self.speechType + "\", \"text\": \"" + self.text + "\"}"


class Card(object):

    def __init__(self, title, subtitle, content, cardType='Simple'):
        self.cardType = cardType
        self.title = title
        self.subtitle = subtitle
        self.content = content
        
    def __str__(self):
        return "{\"type\": \"" + self.cardType + "\", \"title\": \"" + self.title + "\", \"subtitle\": \"" + self.subtitle + "\", \"content\": \"" + self.content + "\"}"
