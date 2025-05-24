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

        def compare_strings(str1, str2):
            compares = 0
            min_len = min(len(str1), len(str2))

            for i in range(min_len):
                compares += 1
                if str1[i] < str2[i]: return -1, compares
                elif str1[i] > str2[i]: return 1, compares

            if len(str1) < len(str2): return -1, compares + 1
            elif len(str1) > len(str2): return 1, compares + 1
            return 0, compares

        def bsearch(T, val, side):
            nonlocal key_fun
            l, r = 0, len(T) - 1
            compares = 0
            while l <= r:
                mid = (l + r) // 2
                comp_result, add_to_comp = compare_strings(val, key_fun(T[mid]))
                compares += add_to_comp
                if comp_result == 0:
                    if side == 0: r = mid - 1
                    elif side == 1: l = mid + 1
                elif comp_result == -1:
                    r = mid - 1
                else:
                    l = mid + 1
            return l, compares
        
        if len(pattern) == 0:
            return [], 0

        m = len(pattern)
        key_fun = lambda x: self.suffix(x)[:m]
        index_l, comp1 = bsearch(self.suffixes, pattern, 0)
        index_r, comp2 = bsearch(self.suffixes, pattern, 1)

        return self.suffixes[index_l:index_r], comp1 + comp2 if self.count_compares else self.suffixes[index_l:index_r]