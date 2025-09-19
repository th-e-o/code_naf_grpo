import os
import requests
import json
from nace_navigator import NACENavigator
import logging 

logger = logging.getLogger(__name__)


class MCPModel():
    '''Class managing the conversation with the llm '''
    def __init__(self, navigator, init_mess=''):
        self.navigator: NACENavigator = navigator
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
                                    "properties": {
                                        "child_code": {"type": "string"}
                                    },
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
        logger.info(f"Messages sent : {messages[-1]} \n")
        data = {
            "model": self.model,
            "messages": messages,
            "tools": self.tools,
            "tool_choice": "any",
            "parallel_tool_calls": False,
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        logger.info(f"Response : {response.json()['choices']} \n")
        return response.json()

    def use_tool(self, call) -> str:
        args = json.loads(call['function']['arguments'] or "{}")
        name = call['function']['name']
        logging.info(f"use_tool function called. Tool {name} called with {args} arguments")

        if name == "get_node_info":
            result = self.navigator.get_node_info(**args)
        elif name == "go_down":
            result = self.navigator.go_down(**args)
        elif name == "go_up":
            result = self.navigator.go_up()
        else:
            result = "Error: unknown tool"
        return result
        