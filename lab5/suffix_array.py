class Suffix:
    def __init__(self, string, index):
        self.string = string
        self.index = index

class SuffixArray:
    def __init__(self, text):
        self.suffixes = [0] * len(text)
        self.text = text
        self.build_array()
        self.count_compares = False

    def suffix(self, i) -> str:
        return self.text[i:]

    def sorted_suffixes(self, text: str) -> list[Suffix]:
        suffixes = []
        n = len(text)
        for i in range(n):
            suffixes.append(Suffix(text[i:], i))
        
        suffixes.sort(key = lambda suff: suff.string)
        return suffixes

    def build_array(self):
        sorted_suff = self.sorted_suffixes(self.text)

        for i, suff in enumerate(sorted_suff):
            self.suffixes[i] = suff.index

    def find_pattern(self, pattern: str):
        i = 0
        n = len(self.suffixes)
        m = len(pattern)
        compares = 0
        while i < n and self.suffix(self.suffixes[i]) < pattern:
            i += 1
            compares += m

        j = i
        while j < n and self.suffix(self.suffixes[j]).startswith(pattern):
            compares += m
            j += 1
        
        if self.count_compares: return self.suffixes[i:j], compares
        return self.suffixes[i:j]