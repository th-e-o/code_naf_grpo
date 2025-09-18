from node import Node
import logging 

logger = logging.getLogger(__name__)


class NACENavigator():
    '''Class for navigate into the NACE tree'''

    def __init__(self, nodes: dict, node: Node):
        self.nodes: dict = nodes
        self.current_node: Node = node

    def to_dict(self) -> dict:
        """
        Return name, description, level, includes/excludes and child codes.
        """
        if self.current_node.children is not None:
            base_info = {
                "code": self.current_node.code,
                "name": self.current_node.name,
                "desc": self.current_node.desc,
                "level": self.current_node.level,
                "parent_code": self.current_node.parent_code,
                "includes": self.current_node.includes,
                "includes_also": self.current_node.includes_also,
                "excludes": self.current_node.excludes,
            }
            children = [c.code for c in self.current_node.children] if self.current_node.children is not None else None
        return {**base_info, "children": children}

    def find_by_code(self, node: Node) -> Node: 
        if node.parent_code in self.nodes: 
            logger.info(f"Node with code {node.parent_code} found")
            return self.nodes[node.parent_code]
        raise ValueError(f"{node.parent_code} is not in the tree")
        
    
    def pretty(self) -> str:
        return self.current_node.pretty()
    
    def get_node_info(self) -> str:
        return str(self.to_dict())

    def get_node_info(self, code) -> str: 
        if code in self.nodes: 
            return str(self.nodes[code].to_dict())
        raise ValueError(f"{code} is not in the tree")

    def go_down(self, child_code: str) -> str:
        for c in self.current_node.children:
            if c.code == child_code:
                self.current_node = c
                return f"Moved to {c.code}: {c.name}"
        raise ValueError(f"{child_code} is not a child of {self.current_node.code}")

    def go_up(self) -> str:
        if self.current_node.parent_code is None:
            return "Already at root."
        self.current_node = self.find_by_code(self.current_node)
        return f"Moved up to {self.current_node.code}: {self.current_node.name}"