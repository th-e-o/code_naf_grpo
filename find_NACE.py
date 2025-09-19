from model_mcp import MCPModel
import json 
from typing import List, Dict


class NACEFinder():
    def __init__(self, company_desc, tries_nb, model_mcp):
        self.company_desc: str = company_desc
        self.tries_nb: int = tries_nb
        self.model_mcp: MCPModel = model_mcp
        system_prompt: dict = {
            "role": "system",
            "content": (
                "You are an autonomous assistant that finds the most relevant NACE classification "
                "leaf for a given company description.\n"
                "You have three tools:\n"
                " • get_node_info(code?):  see details and children of a node.\n"
                " • go_down(child_code):   move to a child node by code.\n"
                " • go_up():               move back to the parent node.\n\n"
                "Goal: navigate the tree from the root until you reach the single best leaf node.\n"
                "If you do not ask for a tool, I will consider that your actual node correspond to the answer.`\n"
                f"You have the right to use {self.tries_nb} times tool calls" 
            ),
        }
        first_message: str = {
            "role": "user",
            "content": (
                f"Company description: {self.company_desc}\n"
                "Start from the root of the NACE tree. "
                "Use the tools step-by-step to inspect nodes and descend "
                "until you are confident you have reached the most specific leaf."
            ),
        }
    
        self.messages = [system_prompt, first_message]

    def leaf_search(self) -> List[Dict]:
        for _ in range(self.tries_nb):
            response = self.model_mcp.request_llm(self.messages)
            message = response['choices'][0]['message']
            self.messages.append(message)
            # If the model requested a tool
            if message['tool_calls']:
                for call in message['tool_calls']:
                    result = self.model_mcp.use_tool(call)
                    # Give the tool result back to the model
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": call['id'],
                        "content": json.dumps(result)
                    })
            else:
                # Model gave a final answer
                return self.messages
                break


        




