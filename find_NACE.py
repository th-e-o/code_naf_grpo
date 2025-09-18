class NACEFinder():
    def __init__(self, company_desc, tries_nb):
        self.company_desc: str = company_desc
        self.tries_nb: int = tries_nb
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
                f"You have the right to use {tries_number} times tool calls" 
            ),
        }
        first_message: str = {
            "role": "user",
            "content": (
                f"Company description: {company_description}\n"
                "Start from the root of the NACE tree. "
                "Use the tools step-by-step to inspect nodes and descend "
                "until you are confident you have reached the most specific leaf."
            ),
        }
    
        self.premier_message = [prompt_message, first_message]
        




