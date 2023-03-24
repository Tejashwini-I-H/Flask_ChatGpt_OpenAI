import json

from CodePilot.CodePilotGateWay import CodePilotGateWay

class CodePilotService:

    def ask(self, query, CodePilotGateWay = CodePilotGateWay()):

        query = "command to find files that start with xyz" 
        self.requestData = ('{'
                       '"model": "gpt-3.5-turbo",'
                       '"messages": [{"role": "user", "content": "' + query + '"}],'
                       '"temperature": 0.7'
                       '}'
                       )
        return CodePilotGateWay.completion(self.requestData)

