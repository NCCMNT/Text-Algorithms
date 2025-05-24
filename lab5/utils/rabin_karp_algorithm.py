def rabin_karp_pattern_match(text: str, pattern: str, prime: int = 101) -> tuple[list[int], int]:
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

    def compare(str1, str2):
        if len(str1) != len(str2): return False, 0
        compares = 0
        for i in range(len(str1)):
            compares += 1
            if str1[i] != str2[i]:
                return False, compares
        return True, compares
    
    def hash(old_hash, oldc):
        return (old_hash + oldc) % prime
    
    def unhash(old_hash, oldc):
        return (old_hash - oldc + prime) % prime

    def hash_string(string):
        hash_res = 0
        for char in string:
            hash_res = hash(hash_res, ord(char))
        return hash_res

    if text == "" or pattern == "": return [], 0

    result = []
    n = len(text)
    m = len(pattern)
    hp = hash_string(pattern)
    htw = hash_string(text[:m])
    compares = 0

    i = 0
    while True:
        if htw == hp and text[i:i+m] == pattern:
            comp_result, add_to_compares = compare(text[i:i+m], pattern)
            compares += add_to_compares
            if comp_result:
                result.append(i)
        
        if n <= i + m:
            break

        htw = hash(htw, ord(text[i+m]))
        htw = unhash(htw, ord(text[i]))
        i += 1
    return result, compares