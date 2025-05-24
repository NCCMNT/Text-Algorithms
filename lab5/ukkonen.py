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
        return f"{self.id}"
        # if isinstance(self.end, End):
        #     return T[self.start : self.end.value] + f" ({self.id})"
        # else:
        #     return T[self.start : self.end] + f" ({self.id})"
 
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
        self.count_compares = False
 
    def build_tree(self):
        """
        Build the suffix tree using Ukkonen's algorithm.
        """
        ID = 0
        END = End(0)

        def split_node(node : Node, last_split : Node = None) -> Node:
            nonlocal ID, END
            parent_node = Node(node.start, node.start + self.active_length)
            # parent_node.id = ID
            # ID += 1

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

            last_split = parent_node
            return last_split
        
        def add_child(node : Node, char, start) -> None:
            nonlocal ID, END
            child = Node(start, END)
            child.id = ID
            ID += 1
            node.children[char] = child
        
        def get_edge_text_len(node : Node):
            return node.end.value - node.start if isinstance(node.end, End) else node.end - node.start

        n = len(self.text)
        for i in range(n):
            char = self.text[i]
            self.remainder += 1
            END.value = i + 1
            last_split = None

            while self.remainder > 0:

                if self.active_length == 0:
                    self.active_edge = i
                edge_char = self.text[self.active_edge]

                if edge_char not in self.active_node.children.keys():
                    add_child(self.active_node, char, i)

                    if last_split is not None:
                        last_split.suffix_link = self.active_node
                        last_split = None
                    if self.active_node is not self.root:
                        self.active_node = self.active_node.suffix_link or self.root
                
                else:
                    node = self.active_node.children[edge_char]
                    edge_len = get_edge_text_len(node)

                    if self.active_length >= edge_len:
                        self.active_node = node
                        self.active_length -= edge_len
                        self.active_edge += edge_len
                        continue

                    if self.text[node.start + self.active_length] == char:
                        self.active_length += 1
                        if last_split:
                            last_split.suffix_link = self.active_node
                        break

                    
                    last_split = split_node(node, last_split)


                    if self.active_node is self.root:
                        self.active_length -= 1
                        self.active_edge += 1
                    else:
                        self.active_node = self.active_node.suffix_link or self.root
                    
                self.remainder -= 1
 
    def find_pattern(self, pattern: str):
        """
        Find all occurrences of the pattern in the text.
 
        Args:
            pattern: The pattern to search for
 
        Returns:
            A list of positions where the pattern occurs in the text
        """
        # Implement pattern search using the suffix tree
        node = self.root
        i = 0
        n = len(pattern)
        compares = 0
        while i < n:
            if pattern[i] not in node.children.keys():
                return []
            compares += 1
            child = node.children[pattern[i]]
            edge_end = child.end.value if isinstance(child.end, End) else child.end
            edge_text = self.text[child.start : edge_end]

            j = 0
            m = len(edge_text)
            while j < m and i < n:
                if pattern[i] != edge_text[j]:
                    return []
                compares += m
                j += 1
                i += 1
            node = child
        
        results = []

        def collect_DFS(node : Node):
            if not node.children:
                results.append(node.id)
                return
            
            for child in node.children.values():
                collect_DFS(child)
        
        collect_DFS(node)
        if self.count_compares: return results, compares
        return results