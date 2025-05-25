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
        low = 0
        high = len(self.text) - 1
        result = []
        n = len(self.text)
        m = len(pattern)
        compares = 0

        while low <= high:
            mid = (low + high) // 2
            suffix_index = self.suffixes[mid]
            i = 0

            while i < m and suffix_index + i < n:
                compares += 1
                if pattern[i] != self.text[suffix_index + i]:
                    break
                i += 1

            if i == m:
                result.append(suffix_index)

                # Left neighbors
                l = mid - 1
                while l >= 0:
                    idx = self.suffixes[l]
                    j = 0
                    while j < m and idx + j < n:
                        compares += 1
                        if pattern[j] != self.text[idx + j]:
                            break
                        j += 1
                    if j == m:
                        result.append(idx)
                        l -= 1
                    else:
                        break

                # Right neighbors
                r = mid + 1
                while r < n:
                    idx = self.suffixes[r]
                    j = 0
                    while j < m and idx + j < n:
                        compares += 1
                        if pattern[j] != self.text[idx + j]:
                            break
                        j += 1
                    if j == m:
                        result.append(idx)
                        r += 1
                    else:
                        break

                if self.count_compares: return result, compares  
                return result

            elif suffix_index + i == len(self.text):
                low = mid + 1
            elif pattern[i] < self.text[suffix_index + i]:
                high = mid - 1
            else:
                low = mid + 1

        if self.count_compares: return [], 0 
        return []