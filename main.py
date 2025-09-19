from model_mcp import MCPModel
from nace_builder import NACEBuilder
from nace_navigator import NACENavigator
import logging 
from find_NACE import NACEFinder

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Main started")
    excel_path = "/home/onyxia/work/code_naf_grpo/NACE_Rev2.1_Structure_Explanatory_Notes_EN.xlsx"
    builder = NACEBuilder()
    nodes, root = builder.build_from_excel(excel_path)
    navigator = NACENavigator(nodes, root)

    mcp_model = MCPModel(navigator)
    company_desc = "[My company sells potatoes]"
    tries_number = 10

    finder = NACEFinder(company_desc, tries_number, mcp_model)

    result = finder.leaf_search()
    print(result)

if __name__ == '__main__':
    main()

