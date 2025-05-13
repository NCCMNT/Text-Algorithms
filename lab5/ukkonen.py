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
        i = 0
        n = len(self.text)
        END = End(None)
        while i < n:
            char = self.text[i]
            END.value = i + 1

            if char not in self.active_node.children.keys():
                current_node = Node(i,END)
                self.active_node.children[char] = current_node
            else:
                self.active_edge = char
                self.active_length += 1
                self.remainder += 1

                node = self.active_node.children[self.active_edge]
                j = 1

                while self.text[node.start + j] == self.text[i + j]:
                    END.value += 1
                    self.active_length += 1
                    self.remainder += 1
                    j += 1

                last_split = None
                while self.remainder >= 1:
                    node = self.active_node.children[self.active_edge]

                    parent_node = Node(node.start, node.start + self.active_length)
                    self.active_node.children[self.text[parent_node.start]] = parent_node

                    if last_split is not None:
                        last_split.suffix_link = parent_node

                    node.start = parent_node.end

                    parent_node.children[self.text[node.start]] = node
                    parent_node.children[self.text[i + j]] = Node(END.value, END)
                    self.active_length -= 1
                    self.remainder -= 1
                    self.active_edge = self.text[parent_node.start + 1]
                    last_split = parent_node
                
                i += j
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

text = 'abcabxabcd'
T = text + '$'
st = SuffixTree(text)
print(st)
