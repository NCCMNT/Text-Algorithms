import pytest

from ukkonen import SuffixTree
import sys
sys.setrecursionlimit(10000)

class TestUkkonen:

    def test_ukkonen_by_number_of_leaves(self):
        short_texts = [
            "abc",
            "aaa",
            "abab",
            "racecar",
            "banana",
            "abcabc",
            "aaaaa",
            "xyzzy",
            "aabbaa",
            "skibidi",
            "addadda"
        ]

        medium_texts = [
            "abracadabrabracabracad",
            "mississippiisreallycool",
            "abcabcabcabcabcabcabcabcabc",
            "zzzyyyxxxyyyzzzzyx",
            "ababababababababababab",
            "abcdabcdabcdabcdabcd",
            "xyzxyzxyzxyzxyzxyzxyzxyz",
            "thequickbrownfoxjumpsoverthelazydog",
            "loremipsumdolorsitametconsectetur",
            "aaaaabbbbbcccccdddddeeeeefffff"
        ]

        long_texts = [
            "a" * 100,
            "ab" * 150,
            "abcde" * 60,
            "banana" * 50,
            "ababababababababababababababababababababababababababa",
            "loremipsum" * 25,
            "zzzyyyxxxwwwvvvuuutttsssrrrqqqpppooonnnmmmlllkkkjjjiii",
            "skibiditoilet" * 20,
            "helloworld" * 30,
            "abcdefghijklmnopqrstuvwxyz" * 4
        ]

        very_long_text = [
            "a" * 512,
            "abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc",
            "abababab" * 70,
            "xyz" * 170 + "end",
            "".join(["abcde"[i % 5] for i in range(600)]),  # cyclic
            "mississippimississippimis",
            "mississippimississippimississippimississippimississippimississippi",
            "Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been."
        ]

        def check_leaves(tree : SuffixTree) -> bool:
            def count_leaves(node):
                if not node.children:
                    return 1
                return sum(count_leaves(child) for child in node.children.values())
            return len(tree.text) == count_leaves(tree.root)

        list = short_texts + medium_texts + long_texts + very_long_text
        for text in list:
            suffix_tree = SuffixTree(text)
            assert check_leaves(suffix_tree)

    def test_ukkonen_finding_pattern(self):

        def test_batch(text : str, patterns : dict) -> bool:
            suffix_tree = SuffixTree(text)
            for pattern, expected in patterns.items():
                result = suffix_tree.find_pattern(pattern)
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