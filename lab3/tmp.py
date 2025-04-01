def naive(pat, text, output):
    for i in range(len(text) - len(pat) + 1):
        if text[i:i+len(pat)] == pat:
            output(i)

def len_of_common_prefix(s, t):
    k = 0
    for k in range(min(len(s), len(t))):
        if s[k] != t[k]:
            return k
    return k

def simple_z_function(s):
    n = len(s)
    z = [0] * n
    for k in range(1, n):
        z[k] = len_of_common_prefix(s[k:], s)
    return z

def z_function(s):
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    for k in range(1,n):
        if k >= r:
            z[k] = len_of_common_prefix(s[k:], s)
            if z[k] > 0:
                l = k
                r = k + z[k]
            elif z[k-l] >= r-k:
                z[k] = r-k + len_of_common_prefix(s[r:], s[r-k:])
                l = k
                r = k + z[k]
            else:
                z[k] = z[k-l]
    return z

print(z_function("nienapełnienie"))
print(simple_z_function("nienapełnienie"))

def backward_has_prefix(s, pat):
    n = len(pat)
    for j in range(n-1,-1,-1):
        if s[j] != pat[j]:
            return False
    return True

def backward_naive(pat, text, output):
    for i in range(len(text) - len(pat) + 1):
        if backward_has_prefix(text[i:], pat):
            output(i)

def find_last_occurrences(s):
    last_occurrences = {}
    for k,c in enumerate(s):
        last_occurrences[c] = k + 1
    return last_occurrences

def boyer_moore_horspool_has_prefix(pat, text, last_occurrences):
    for j in range(len(pat) - 1, -1, -1):
        if text[j] != pat[j]:
            return False, max(j + 1 - last_occurrences.get(text[j],0), 1)
    return True, 1

def boyer_moore_horspool(pat, text, output):
    last_occurrences = find_last_occurrences(pat)
    i = 0
    while i + len(pat) <= len(text):
        found, shift = boyer_moore_horspool_has_prefix(pat, text[i:], last_occurrences)
        if found:
            output(i)
        i += shift




def simple_find_shift_of_suffix(s, i):
    for k in range(1, i+1):
        print(s[i-k], s[i], s[i+1:], s[i-k+1 : len(s)-k])
        if s[i-k] != s[i] and s[i+1:] == s[i-k+1 : len(s)-k]:
            return k
    for k in range(i+1, len(s)):
        print(s[k:], s[:len(s)-k])
        if s[k:] == s[:len(s)-k]:
            return k
    return len(s)

a = simple_find_shift_of_suffix("dźwiedź", 3)
print(a)


def kpm_prefix_function(s):
    z = z_function(s)
    p = [0] * (len(s) + 1)
    for j in range(len(s) - 1, 0, -1):
        p[j + z[j]] = z[j]
    return p

def hash_byte_mod_n(b,h,n):
    h = ((h << 8) | b) % n
    return h

def hash_bytes_mod_n(bs, n):
    h = 0
    for b in bs:
        h = hash_byte_mod_n(b,h,n)
    return h

def two_to_power_8p_mod_n(p,n):
    result = 1
    for i in range(p):
        power = 8 * i
        result = pow(2, power, n)
    return result

def unhash_byte_mod_n(b,h,n,power):
    r = h - power * b
    if r < 0:
        r += n * ((-r // n) + 1)
    return r % n

def karp_rabin(pat, text, output_func):
    N = 2 ** 61 - 1
    h = hash_bytes_mod_n(text[:len(pat)], N)
    ph = hash_bytes_mod_n(pat, N)
    power = two_to_power_8p_mod_n(len(pat), N)
    i = 0
    while True:
        if h == ph and pat == text[i:i+len(pat)]:
            output_func(i)
        if i + len(pat) >= len(text):
            break
        h = hash_byte_mod_n(text[i+len(pat)], h, N)
        h = unhash_byte_mod_n(text[i], h, N, power)
        i += 1