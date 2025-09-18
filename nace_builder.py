import pandas as pd

class NACEBuilder():
    '''Class to build the tree of the NACE classification from the excel defining the NACE classification'''
    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.nodes = {}
        self.root = None
    
    def build_from_excel(self, filename: str = None):
        """Build NACE graph from your Excel file"""
        file_to_use = filename if filename is not None else self.excel_path
        # Load Excel
        df = pd.read_excel(file_to_use)
        print(f"✅ Loaded {len(df)} entries")
        
        # Create all nodes
        for _, row in df.iterrows():
            node = Node(
                code=str(row['CODE']),
                name=row['NAME'],
                desc=row['NAME'],  # Using name as desc
                level=int(row['LEVEL']),
                parent_code=row['PARENT_CODE'] if pd.notna(row['PARENT_CODE']) else None,
                includes=row['Includes'] if pd.notna(row['Includes']) else None,
                includes_also=row['IncludesAlso'] if pd.notna(row['IncludesAlso']) else None,
                excludes=row['Excludes'] if pd.notna(row['Excludes']) else None,
                implementation_rule=row['Implementation_rule'] if pd.notna(row['Implementation_rule']) else None
            )
            self.nodes[node.code] = node
        
        # Build relationships
        for node in self.nodes.values():
            if node.parent_code and node.parent_code in self.nodes:
                parent = self.nodes[node.parent_code]
                parent.add_child(node)
        
        # Find root
        roots = [n for n in self.nodes.values() if not n.parent_code]
        
        if len(roots) == 1:
            self.root = roots[0]
        else:
            # Create artificial root
            self.root = Node(
                code='NACE',
                name='NACE Rev. 2.1',
                desc='Statistical Classification of Economic Activities',
                level=0
            )
            for root in roots:
                self.root.add_child(root)
        
        print(f"✅ Built graph with {len(self.nodes)} nodes")
        return self.root

