import os
import requests


class MCPModel():
    '''Class managing the conversation with the llm '''
    def __init__(self, init_mess=''):
        self.model = "gpt-oss:20b"
        self.token = os.environ["GPT_OS_KEY"]
        self.url = 'https://llm.lab.sspcloud.fr/api/chat/completions'
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        
    def request_llm(self, messages, tools=[]):
        data = {
            "model": self.model,
            "messages": messages,
            "tools": tools,
            "tool_choice": "any",
            "parallel_tool_calls": False,
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()