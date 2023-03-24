import unittest
from unittest.mock import MagicMock
from CodePilot.CodePilotService import CodePilotService

class TestCodePilotService(unittest.TestCase):
    
    def test_code_pilot_service(self):
        self.query = "command to find files that start with xyz"
        self.CodePilotGateWayMock = MagicMock()
        self.service_obj = CodePilotService()
        self.api_response = self.service_obj.ask(self.query, self.CodePilotGateWayMock)
        self.requestData = ('{'
                       '"model": "gpt-3.5-turbo",'
                       '"messages": [{"role": "user", "content": "' + self.query + '"}],'
                       '"temperature": 0.7'
                       '}'
                       )
        self.CodePilotGateWayMock.completion.assert_called_with(self.requestData)

        # assert self.api_response["command"] != None
        # assert self.api_response["info"] != None
