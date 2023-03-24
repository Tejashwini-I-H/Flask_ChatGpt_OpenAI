import json
from flask import Flask
import flask_unittest
import requests
import os
import sys

from CodePilot.ResponseParser import jsonParser

app = Flask(__name__)

class CodePilotGateWay():

    def __init__(self):
        self.jsonparser = jsonParser()

    def completion(self,request_data):
        api_key = os.getenv('CHATGPT_API_KEY')
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {api_key}"}
        
        response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers = headers, 
                             json = json.loads(request_data))
        
        self.jsonparser.set_api_response(response.text)
        self.jsonparser.parse_api_response()
        return self.jsonparser.prepare_json_from_api_response()
    
  

