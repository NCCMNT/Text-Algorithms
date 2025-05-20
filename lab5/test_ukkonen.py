from ukkonen_cp2 import SuffixTree
import sys
sys.setrecursionlimit(10000)

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
    "skibidi"
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
    "mississippimississippimississippimississippimississippimississippi"
]


def test_ukkonen_by_number_of_leaves(list : list, testno : int) -> bool:

    def check_leaves(tree : SuffixTree) -> bool:
        def count_leaves(node):
            if not node.children:
                return 1
            return sum(count_leaves(child) for child in node.children.values())
        return len(tree.text) == count_leaves(tree.root)

    for text in list:
        suffix_tree = SuffixTree(text)
        if not check_leaves(suffix_tree):
            print(f"Test {testno} failed on: {text}")
            return False
    print(f"Test {testno} passsed")
    return True

def run_tests():
    leaves_tests_batch = [short_texts, medium_texts, long_texts, very_long_text]
    for i, batch in enumerate(leaves_tests_batch):
        if not test_ukkonen_by_number_of_leaves(batch, i):
            return False

run_tests()