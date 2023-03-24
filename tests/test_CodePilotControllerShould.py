import unittest
from unittest.mock import MagicMock

from CodePilot.CodePilotController import ask

class TestCodePilotController(unittest.TestCase):

    def test_controller_ask(self):
        self.query = "command to find files that start with xyz"
        self.ServiceMock = MagicMock()
        ask(self.query, self.ServiceMock)
        self.ServiceMock.ask.assert_called_with(self.query)


    
    


    
        




      
    