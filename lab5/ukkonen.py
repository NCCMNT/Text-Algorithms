class End:
    def __init__(self, value):
        self.value = value

class Node:
    def __init__(self, start, end):
        self.children = {}
        self.suffix_link = None
        self.start = start
        self.end = end
        self.id = -1
    def __repr__(self):
        if isinstance(self.end, End):
            return T[self.start : self.end.value]
        else:
            return T[self.start : self.end]
 
class SuffixTree:
    def __init__(self, text: str):
        """
        Construct a suffix tree for the given text using Ukkonen's algorithm.
 
        Args:
            text: The input text for which to build the suffix tree
        """
        self.text = text + "$"
        self.root = Node(None, None)
        self.active_node = self.root
        self.active_edge = 0
        self.active_length = 0
        self.remainder = 0
        self.build_tree()
 
    def build_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm.
        """
        def get_edge_text_len(node : Node):
            return node.end.value - node.start if isinstance(node.end, End) else node.end - node.start

        ID = 1
        END = End(0)

        def split_node(node : Node, last_split : Node = None) -> Node:
            nonlocal ID, END
            parent_node = Node(node.start, node.start + self.active_length)
            parent_node.id = ID
            ID += 1
            self.active_node.children[self.text[parent_node.start]] = parent_node

            # Rule 2
            if last_split is not None:
                last_split.suffix_link = parent_node
            
            node.start = parent_node.end
            new_leaf = Node(END.value - 1, END)
            new_leaf.id = ID
            ID += 1

            parent_node.children[self.text[node.start]] = node
            parent_node.children[self.text[new_leaf.start]] = new_leaf

            self.remainder -= 1
            self.active_length -= 1       
            last_split = parent_node
            return last_split
        
        def add_child(node : Node, char, start) -> None:
            nonlocal ID, END
            child = Node(start, END)
            child.id = ID
            ID += 1
            node.children[char] = child

        i = 0
        n = len(self.text)
        END = End(None)
        while i < n:
            char = self.text[i]
            END.value = i + 1
            self.remainder = 1

            if char not in self.active_node.children.keys():
                add_child(self.active_node, char, i)

            else:
                node = self.active_node.children[char]
                self.active_edge = char
                self.active_length = 1
                self.remainder += 1


                
            
            i += 1


 
    def find_pattern(self, pattern: str) -> list[int]:
        """
        Find all occurrences of the pattern in the text.
 
        Args:
            pattern: The pattern to search for
 
        Returns:
            A list of positions where the pattern occurs in the text
        """
        # Implement pattern search using the suffix tree
        pass

text = 'abcabxabcd'
T = text + '$'
st = SuffixTree(text)
print(st)
