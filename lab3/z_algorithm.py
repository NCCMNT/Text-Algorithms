def compute_z_array(s: str) -> list[int]:
    """
    Compute the Z array for a string.

    The Z array Z[i] gives the length of the longest substring starting at position i
    that is also a prefix of the string.

    Args:
        s: The input string

    Returns:
        The Z array for the string
    """
    # TODO: Implement the Z-array computation
    # For each position i:
    # - Calculate the length of the longest substring starting at i that is also a prefix of s
    # - Use the Z-box technique to avoid redundant character comparisons
    # - Handle the cases when i is inside or outside the current Z-box

    def common_prefix(s1, s2):
        n = len(s1)
        m = len(s2)
        for i in range(min(n,m)):
            if s1[i] != s2[i]:
                return i
        return m

    n = len(s)
    z = [0] * n
    for i in range(1,n):
        z[i] = common_prefix(s, s[i:])  

    return z


def z_pattern_match(text: str, pattern: str) -> list[int]:
    """
    Use the Z algorithm to find all occurrences of a pattern in a text.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement pattern matching using the Z algorithm
    # 1. Create a concatenated string: pattern + special_character + text
    # 2. Compute the Z array for this concatenated string
    # 3. Find positions where Z[i] equals the pattern length
    # 4. Convert these positions in the concatenated string to positions in the original text
    # 5. Return all positions where the pattern is found in the text
    if pattern == "": return []
    m = len(pattern)
    result = []
    cs = pattern + "\t" + text
    z = compute_z_array(cs)
    for i in range(len(z)):
        if z[i] == m:
            result.append(i - m - 1)

    return result