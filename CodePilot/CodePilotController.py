
from flask import Flask
import os
import sys


from CodePilot.CodePilotService import CodePilotService

app = Flask(__name__)

@app.route("/code-pilot/ask/<query>")
def ask(query, CodePilotService = CodePilotService()):
    return CodePilotService.ask(query)

if __name__ == "__main__":
    app.run()
        
