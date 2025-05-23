import pytest
from suffix_array import SuffixArray

class TestSuffixArray:
    def test_array_finding_pattern(self):

        def test_batch(text : str, patterns : dict) -> bool:
            suffix_array = SuffixArray(text)
            for pattern, expected in patterns.items():
                result = suffix_array.find_pattern(pattern)
                result.sort()
                assert result == expected, f"Failed for pattern '{pattern}': got {result}, expected {expected}"
            print(f"PASSED pattern matching test")
            return True

        assert test_batch("abracadabra", {
            "abra": [0, 7],
            "cad": [4],
            "a": [0, 3, 5, 7, 10],
            "ra": [2, 9],
            "xyz": [],
        })

        assert test_batch("banana", {
            "na": [2, 4],
            "ana": [1, 3],
            "nana": [2],
            "banana": [0],
            "bananas": [],
        })

        assert test_batch("abracad" * 50, {"abra" : list(range(0,350,7))})
        assert test_batch("Nory was a Catholic because her mother was a Catholic, and Nory’s" \
        " mother was a Catholic because her father was a Catholic, and her father was a Catholic" \
        " because his mother was a Catholic, or had been.", {"Catholic" : [11, 45, 79, 113, 144, 178]})