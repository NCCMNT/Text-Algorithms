def naive_pattern_match(text: str, pattern: str) -> list[int]:
    """
    Implementation of the naive pattern matching algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement the naive pattern matching algorithm
    # This is the most straightforward approach to string matching:
    # 1. Check every possible starting position in the text
    # 2. For each position, compare the pattern with the text character by character
    # 3. If all characters match, add the starting position to the results
    # 4. Handle edge cases like empty patterns and patterns longer than the text
    if pattern == "": return []

    def compare(str1, str2):
        if len(str1) != len(str2): return False, 0
        compares = 0
        for i in range(len(str1)):
            compares += 1
            if str1[i] != str2[i]:
                return False, compares
        return True, compares

    n = len(text)
    m = len(pattern)
    result = []
    compares = 0
    for i in range(n):
        comp_result, add_to_compares = compare(text[i:i+m], pattern)
        if comp_result:
            result.append(i)
        compares += add_to_compares

    return result, compares