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
        # return self.id
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
        ID = 1
        END = End(None)

        def split_node(node : Node, last_split : Node = None) -> Node:
            nonlocal ID, END
            parent_node = Node(node.start, node.start + self.active_length)
            parent_node.id = ID
            ID += 1
            self.active_node.children[self.text[parent_node.start]] = parent_node

            if last_split is not None:
                last_split.suffix_link = parent_node
            
            node.start = parent_node.end
            new_node = Node(END.value - 1, END)
            new_node.id = ID
            ID += 1

            parent_node.children[self.text[node.start]] = node
            parent_node.children[self.text[new_node.start]] = new_node

            self.remainder -= 1
            self.active_length -= 1
            if self.active_length > 0: 
                self.active_edge = self.text[parent_node.start + 1]
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
        while i < n:
            char = self.text[i]
            END.value = i + 1

            if char not in self.active_node.children.keys():
                add_child(self.active_node, char, i)
            
            else:
                self.active_length = 0
                self.remainder = 0
                self.active_edge = char
                node = self.active_node.children[char]

                next_char_in_text = self.text[i]
                next_char_in_edge = self.text[node.start]
                j = 0
                index = 0
                while next_char_in_edge == next_char_in_text:
                    END.value += 1
                    self.active_length += 1
                    self.remainder += 1
                    j += 1
                    index += 1

                    next_char_in_text = self.text[i + index]

                    edge_end = node.end.value if isinstance(node.end, End) else node.end
                    if index == (edge_end - node.start):
                        self.active_node = node
                        self.active_length = 0
                        self.active_edge = 0 #None
                        if next_char_in_text in self.active_node.children.keys():
                            node = self.active_node.children[next_char_in_text]
                            next_char_in_edge = self.text[node.start]
                            self.active_edge = next_char_in_edge
                            j = 0
                            edge_end = node.end.value if isinstance(node.end, End) else node.end
                            continue
                        else:
                            break

                    next_char_in_edge = self.text[node.start + j]

                last_split = None
                while self.remainder >= 1:
                    if self.active_edge != 0:
                        node = self.active_node.children[self.active_edge]
                        last_split = split_node(node, last_split)
                    else:
                        add_child(self.active_node, next_char_in_text, i+index)
                        self.remainder -= 1

                    if self.active_node is not self.root:
                        self.active_length += 1
                        if self.active_node.suffix_link is not None:
                            self.active_node = self.active_node.suffix_link
                        else:
                            self.active_node = self.root
                
                i += index
                continue
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

# text = 'abcabxabcd'
# T = text + '$'
# st = SuffixTree(text)
# print(st)

# t2 = 'ababadda'
# T = t2 + '$'
# st = SuffixTree(t2)
# print(st)

