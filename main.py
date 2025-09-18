from model_mcp import MCPModel
from nace_builder import NACEBuilder
from nace_navigator import NACENavigator
import logging 


def main():
    excel_path = "/home/onyxia/work/code_naf_grpo/NACE_Rev2.1_Structure_Explanatory_Notes_EN.xlsx"
    builder = NACEBuilder()
    nodes, root = builder.build_from_excel(excel_path)
    navigator = NACENavigator(nodes, root)
    print(navigator.get_node_info())

    mcp_model = MCPModel()

    company_description = "[My company sells potatoes]"
    tries_number = 100
    messages = [,
        ,
    ]
    
if __name__ == '__main__':
    main()

