class Suffix:
    def __init__(self, string, index):
        self.string = string
        self.index = index  

class SuffixArray:
    def __init__(self, suffixes, text):
        self.suffixes = suffixes
        self.text = text

def sorted_suffixes(text: str) -> list[int]:
    suffixes = []
    n = len(text)
    for i in range(n):
        suffixes.append(Suffix(text[i:], i))
    
    suffixes.sort(key = lambda suff: suff.string)
    return suffixes

def suffix_array(text: str) -> SuffixArray:
    n = len(text)
    sa = SuffixArray([0] * n, bytearray(n))
    sa.text = text

    sorted_suff = sorted_suffixes(text)

    for i, suff in enumerate(sorted_suff):
        sa.suffixes[i] = suff.n

    return sa
