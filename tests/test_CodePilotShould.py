
import flask_unittest

import json

from CodePilot.CodePilotController import app

# Integration Test Code
class TestCodePilot(flask_unittest.ClientTestCase):

    app = app

    def test_when_queried_responds_back_with_command(self, client):
        query = "command to find files that start with xyz"
        
        response = client.get("/code-pilot/ask/" + query)
        response = json.loads(response.text)
      
        assert response["command"] != None
        assert response["content"] != None 
        assert response["info"] != None 


        
       
