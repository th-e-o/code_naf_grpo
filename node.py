from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node():
    code: str
    name: str
    desc: str
    level: int
    parent_code: Optional[str] = None
    implementation_rule: Optional[str] = None
    includes: Optional[str] = None
    includes_also: Optional[str] = None
    excludes: Optional[str] = None
    children: Optional[List[Node]] = None

    def get_name(self) -> str:
        return self.name
        
    def get_desc(self) -> str:
        return self.desc
        
    def has_children(self) -> bool:
        return self.children is not None and len(self.children) > 0
        
    def get_children(self) -> Optional[List['Node']]:
        return self.children
    
    def add_child(self, child: 'Node'):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def add_parent(self, parent: str):
        self.parent_code = parent
    
    def count_descendants(self) -> int:
        if not self.has_children():
            return 0
        count = len(self.children)
        for child in self.children:
            count += child.count_descendants()
        return count
  
    def find_by_code(self, target_code: str) -> Optional['Node']:
        if self.code == target_code:
            return self
        if self.has_children():
            for child in self.children:
                result = child.find_by_code(target_code)
                if result:
                    return result
        return None

    def pretty(self, indent: int = 2) -> str:
        pad = "  " * indent
        s = f"{pad}{self.code}: {self.name}"
        if self.children is not None:
            for child in self.children:
                s += "\n" + child.pretty(indent + 1)
        return s
