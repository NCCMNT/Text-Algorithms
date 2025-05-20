from ukkonen import SuffixTree, Node
import random, string

def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring of two strings using a suffix tree.
 
    Args:
        str1: First string
        str2: Second string
 
    Returns:
        The longest common substring
    """
    # Concatenate the strings with a unique separator
    combined = str1 + "#" + str2 + "$"
    seperator_index = len(str1)
    longest_substring = ""
 
    # Build a suffix tree for the combined string
    st = SuffixTree(combined)

    # Traverse the tree to find the longest path that occurs in both strings
    def DFS(node : Node, path : list):
        nonlocal longest_substring
        bits = set()

        if not node.children:
            if node.id < seperator_index:
                bits.add(0)
            elif node.id > seperator_index:
                bits.add(1)
            return bits
        
        for child in node.children.values():
            edge_end = child.end.value if hasattr(child.end, 'value') else child.end
            edge_text = st.text[child.start : edge_end]

            bits.update(DFS(child, path + [edge_text]))

        if 0 in bits and 1 in bits:
            substring = "".join(path)
            if len(substring) > len(longest_substring):
                longest_substring = substring

        return bits
    
    DFS(st.root, [])
    return longest_substring
 
def longest_common_substring_multiple(strings: list[str]) -> str:
    """
    Find the longest common substring among multiple strings using suffix structures.
 
    Args:
        strings: List of strings to compare
 
    Returns:
        The longest common substring that appears in all strings
    """
    # Implement an algorithm to find the longest common substring in multiple strings
    # You may use either suffix trees or suffix arrays
    
    n = len(strings)
        # Concatenate the strings with a unique separator
    if n == 0: return ""
    if n == 1: return strings[0]

    combined = ""
    seperator_indexes = []
    available_separators = list(set(string.punctuation) - set(["".join(s) for s in strings]))
    seperators = random.sample(available_separators, n)

    j = 0
    for i, str in enumerate(strings):
        combined += str + seperators[i]
        seperator_indexes.append((j, j + len(str)))
        j += len(str) + 1
    longest_substring = ""
 
    # Build a suffix tree for the combined string
    st = SuffixTree(combined)

    # Traverse the tree to find the longest path that occurs in both strings
    def DFS(node : Node, path : list):
        nonlocal longest_substring
        bits = set()

        if not node.children:
            for k, (start, end) in enumerate(seperator_indexes):
                if start <= node.id < end:
                    bits.add(k)
                    break
            return bits
        
        for child in node.children.values():
            edge_end = child.end.value if hasattr(child.end, 'value') else child.end
            edge_text = st.text[child.start : edge_end]

            bits.update(DFS(child, path + [edge_text]))

        if len(bits) == n:
            substring = "".join(path)
            if len(substring) > len(longest_substring):
                longest_substring = substring

        return bits
    
    DFS(st.root, [])
    return longest_substring
 
def longest_palindromic_substring(text: str) -> str:
    """
    Find the longest palindromic substring in a given text using suffix structures.
 
    Args:
        text: Input text
 
    Returns:
        The longest palindromic substring
    """
    # Create a new string concatenating the original text and its reverse
    # Use suffix structures to find the longest common substring between them
    # Handle the case where palindrome centers between characters
    combined = text + "#" + text[::-1] + "$"
    st = SuffixTree(combined)
 
    pass