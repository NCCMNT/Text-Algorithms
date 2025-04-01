def rabin_karp_pattern_match(text: str, pattern: str, prime: int = 101) -> list[int]:
    """
    Implementation of the Rabin-Karp pattern matching algorithm.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        prime: A prime number used for the hash function

    Returns:
        A list of starting positions (0-indexed) where the pattern was found in the text
    """
    # TODO: Implement the Rabin-Karp string matching algorithm
    # This algorithm uses hashing to find pattern matches:
    # 1. Compute the hash value of the pattern
    # 2. Compute the hash value of each text window of length equal to pattern length
    # 3. If the hash values match, verify character by character to avoid hash collisions
    # 4. Use rolling hash to efficiently compute hash values of text windows
    # 5. Return all positions where the pattern is found in the text
    # Note: Use the provided prime parameter for the hash function to avoid collisions
    BASE = 256

    def hash(s: str):
        h = 0
        for i, c in enumerate(s):
            h += ord(c) * (BASE ** i)
        return h % prime
    
    def rolling_hash(old_hash, oldc, newc, pattern_len):
        return (old_hash - ord(oldc) * (BASE ** (pattern_len - 1))) * BASE + ord(newc)

    if text == "" or pattern == "": return []

    result = []
    n = len(text)
    m = len(pattern)
    hp = hash(pattern)
    htw = hash(text[:m])

    if htw == hp and text[:m] == pattern:
        result.append(0)

    for i in range(1, n - m + 1):
        htw = rolling_hash(htw, text[i-1], text[m+i-1], m)

        if htw == hp and text[i:i+m] == pattern:
            result.append(i)

    return result

text = "ABABDABACDABABCABAB"
pattern = "ABABC"

print(rabin_karp_pattern_match(text, pattern))