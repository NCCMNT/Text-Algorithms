from ukkonen import SuffixTree, Node
from suffix_array import SuffixArray, Suffix
import time, psutil, os, sys

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024  # in KB

def get_suffix_tree_size(st: SuffixTree):
    size_of_node = sys.getsizeof(Node(None, None))

    def dfs(node: Node):
        total = size_of_node
        
        for child in node.children.values():
            total += dfs(child)
        return total
    
    return dfs(st.root)

def get_suffix_array_size(sa: SuffixArray):
    size_of_suffix = sys.getsizeof(Suffix("", None))
    return len(sa.suffixes) * size_of_suffix

def compare_suffix_structures(text: str) -> dict:
    """
    Compare suffix array and suffix tree data structures.
 
    Args:
        text: The input text for which to build the structures
 
    Returns:
        A dictionary containing:
        - Construction time for both structures
        - Memory usage for both structures
        - Size (number of nodes/elements) of both structures
    """
    prior_mem = get_memory_usage()

    # Measure time and memory usage
    start_time = time.time()
    sa = SuffixArray(text)
    end_time = time.time()
    sarray_construction = (end_time - start_time) * 1000
    mem_after_sa = get_memory_usage()
    sarray_mem_usage = mem_after_sa - prior_mem

    start_time = time.time()
    st = SuffixTree(text)
    end_time = time.time()
    stree_construction = (end_time - start_time) * 1000
    mem_after_st = get_memory_usage()
    stree_mem_usage = mem_after_st - mem_after_sa
    
    # Measure size of structures in bytes
    sarray_size = get_suffix_array_size(sa)
    stree_size = get_suffix_tree_size(st)

    return {
        "suffix_array": {
            "construction_time_ms": sarray_construction,
            "memory_usage_kb": sarray_mem_usage,
            "size": sarray_size
        },
        "suffix_tree": {
            "construction_time_ms": stree_construction,
            "memory_usage_kb": stree_mem_usage,
            "size": stree_size
        }
    }