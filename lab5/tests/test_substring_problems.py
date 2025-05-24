import pytest

from substring_problems import longest_common_substring_sa, longest_common_substring_st, longest_palindromic_substring, longest_common_substring_multiple

class TestSubstringProblems:
    def test_lcs_sa(self):
        test_cases = [
            ("abcdef", "abc", "abc"),
            ("xyz", "abc", ""),
            ("banana", "banana", "banana"),
            ("hello", "lo", "lo"),
            ("startmatch", "start", "start"),
            ("abracadabra", "racad", "racad"),
            ("bajojajo bajojajo", "ja ci dam pajacu bajojajo", " bajojajo"),
            ("abababababab", "bababababa", "bababababa"),
            ("Zażółć gęślą jaźń", "gęślą", "gęślą"),
            ("abcdef", "", ""),
            ("", "", ""),
            ("x", "x", "x"),
            ("abcxyz123", "xyx789abc", "abc"),
            ("aaaaabbbbcccc", "xxxbbbbyyyy", "bbbb"),
            ("testlongest", "longest", "longest"),
            ("prefixmatch", "matchpostfix", "match"),
            ("hello, world!", "world!", "world!"),
            ("hello😀world", "😀wo", "😀wo"),
        ]

        for s1, s2, expected in test_cases:
            result = longest_common_substring_sa(s1,s2)
            assert result == expected

    def test_lcs_st(self):
        test_cases = [
            ("abcdef", "abc", "abc"),
            ("xyz", "abc", ""),
            ("banana", "banana", "banana"),
            ("hello", "lo", "lo"),
            ("startmatch", "start", "start"),
            ("abracadabra", "racad", "racad"),
            ("bajojajo bajojajo", "ja ci dam pajacu bajojajo", " bajojajo"),
            ("abababababab", "bababababa", "bababababa"),
            ("Zażółć gęślą jaźń", "gęślą", "gęślą"),
            ("abcdef", "", ""),
            ("", "", ""),
            ("x", "x", "x"),
            ("abcxyz123", "xyx789abc", "abc"),
            ("aaaaabbbbcccc", "xxxbbbbyyyy", "bbbb"),
            ("testlongest", "longest", "longest"),
            ("prefixmatch", "matchpostfix", "match"),
            ("hello, world!", "world!", "world!"),
            ("hello😀world", "😀wo", "😀wo"),
        ]

        for s1, s2, expected in test_cases:
            result = longest_common_substring_st(s1,s2)
            assert result == expected

    def test_multiple_lcs(self):
        test_cases = {
            ("abc", "abc"): "abc",
            ("abc", "def"): "",
            ("abcde", "cdefg", "defgh"): "de",
            ("ababab", "babab", "abab"): "abab",
            ("aaaa", "aa", "aaa"): "aa",
            ("racecar", "myrace", "racing"): "rac",
            ("abcXXXXcba", "abc123cba", "zzzcbayy"): "cba",
            ("a#b@c", "#b@c$d", "@c$def"): "@c",
            ("123!abc", "!abc456", "xyz!abc"): "!abc",
            ("",): "",
            ("abc",): "abc",
            (): "",
            ("banana", "ananas", "bandana"): "ana",
            ("thequickbrownfox", "quickfox", "lazyquickfox"): "quick",
            ("123456", "456789", "0456123"): "456",
            ("👀hello👋", "👋hello", "sayhello👋"): "hello",
        }

        for strings, expected in test_cases.items():
            result = longest_common_substring_multiple(strings)
            assert result == expected

    def test_palindrome(self):
        test_cases = {
            "cbbd": "bb",
            "a": "a",
            "racecar": "racecar",
            "abacdfgdcaba": "aba",
            "": "",
            "abcddcbazzz": "abcddcba",
            "banana": "anana",
            "level": "level",
            "aaabaaaa": "aaabaaa",
            "xyzzyx": "xyzzyx",
            "bajojab cd ad d" : "bajojab",
        }

        for text, expected in test_cases.items():
            result = longest_palindromic_substring(text)
            assert result == expected