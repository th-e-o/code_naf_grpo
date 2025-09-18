import os
import requests
import json


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
        self.tools = [
                        {
                            "type": "function",
                            "function": {
                                "name": "get_node_info",
                                "description": "Get details of the current node.",
                                "parameters": {
                                    "type": "object",
                                    "required": [],
                                },
                            },
                        },
                        {
                            "type": "function",
                            "function": {
                                "name": "go_down",
                                "description": "Move to a child node by code.",
                                "parameters": {
                                    "type": "object",
                                    "properties": {
                                        "child_code": {"type": "string"}
                                    },
                                    "required": ["child_code"],
                                },
                            },
                        },
                        {
                            "type": "function",
                            "function": {
                                "name": "go_up",
                                "description": "Move to the parent node.",
                                "parameters": {"type": "object", "properties": {}},
                            },
                        },
                    ]

    def request_llm(self, messages) -> json:
        data = {
            "model": self.model,
            "messages": messages,
            "tools": self.tools,
            "tool_choice": "any",
            "parallel_tool_calls": False,
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()