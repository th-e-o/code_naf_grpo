from model_mcp import MCPModel
from nace_builder import NACEBuilder
from nace_navigator import NACENavigator


def main():
    excel_path = "/home/onyxia/work/code_naf_grpo/NACE_Rev2.1_Structure_Explanatory_Notes_EN.xlsx"
    navigator = NACENavigator(NACEBuilder(excel_path))
    mcp_model = MCPModel()



'''
    tries_number = 10

    for _ in range(tries_number):
        # Ask the model
        response = chat_with_model(api_key_llm_lab, messages, tools)

        message = response['choices'][0]['message']
        messages.append(message)
        # If the model requested a tool
        if message['tool_calls']:
            for call in message['tool_calls']:
                args = json.loads(call['function']['arguments'] or "{}")
                name = call['function']['name']

                if name == "get_node_info":
                    result = get_node_info()
                elif name == "go_down":
                    result = go_down(**args)
                elif name == "go_up":
                    result = go_up()
                else:
                    result = {"error": "unknown tool"}

                # Give the tool result back to the model
                messages.append({
                    "role": "tool",
                    "tool_call_id": call['id'],
                    "content": json.dumps(result)
                })
        else:
            # Model gave a final answer
            break

    for message in messages:
        print(message)
        print("\n \n")
'''
if __name__ == '__main__': 
    main()