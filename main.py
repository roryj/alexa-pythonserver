#!/usr/bin/python

from flask import Flask, request
import json
from src.alexarequest import AlexaRequest
from src.alexaresponse import AlexaResponse
from src.response import OutputSpeech, Card

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/alexa', methods=['POST'])
def handle_alexa_request():

    alexaRequest = json.loads(request.data.decode("utf-8"))

    # print (alexaRequest)

    test = AlexaRequest(alexaRequest)

    print(test.session.getUserId())

    # print (result["version"])
    # j = json.loads(test)
    # print (j['version'])
    return 'test'


@app.route('/yesterday')
def oranages():
    card = Card(title='Test', subtitle='The best card', content='This is a card')
    speech = OutputSpeech(text='Say this bitch.')
    
    sessionAttributes = { 'supportedHoriscopePeriods': 
        {
          'daily': True,
          'weekly': False,
          'monthly': False
          }
      }
    
    response = AlexaResponse(sessionAttributes, speech, card, True)

    print(response)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
