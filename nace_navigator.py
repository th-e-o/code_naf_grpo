class NACENavigator():
    '''Class for navigate into the NACE tree'''

    def __init__(self, node):
        self.current_node = node

    def to_dict(self) -> dict:
        """
        Return name, description, level, includes/excludes and child codes.
        """
        if self.current_node.children is not None:
            result = {
                "code": self.current_node.code,
                "name": self.current_node.name,
                "desc": self.current_node.desc,
                "level": self.current_node.level,
                "parent_code": self.current_node.parent_code,
                "includes": self.current_node.includes,
                "includes_also": self.current_node.includes_also,
                "excludes": self.current_node.excludes,
                "children": [c.code for c in self.current_node.children],
            }
        else:
            result = {
                "code": self.current_node.code,
                "name": self.current_node.name,
                "desc": self.current_node.desc,
                "level": self.current_node.level,
                "parent_code": self.current_node.parent_code,
                "includes": self.current_node.includes,
                "includes_also": self.current_node.includes_also,
                "excludes": self.current_node.excludes,
                "children": None,
            }
        return result

    def get_node_info(self) -> str:
        return str(self.to_dict())

    def go_down(self, child_code: str) -> str:
        for c in self.node.children:
            if c.code == child_code:
                self.current_node = c
                return f"Moved to {c.code}: {c.name}"
        raise ValueError(f"{child_code} is not a child of {self.current_node.code}")

    def go_up(self) -> str:
        if self.current_node.parent_code is None:
            return "Already at root."
        self.current_node = self.current_node.find_by_code(navigator.root, navigator.current.parent_code)
        return f"Moved up to {parent.code}: {parent.name}"