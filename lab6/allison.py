def allison_global_alignment(s1: str, s2: str,
                           match_score: int = 2,
                           mismatch_score: int = -1,
                           gap_penalty: int = -1) -> tuple[int, str, str]:
    """
    Znajduje optymalne globalne wyrównanie używając algorytmu Allisona.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków
        match_score: Punkty za dopasowanie
        mismatch_score: Punkty za niedopasowanie
        gap_penalty: Kara za lukę

    Returns:
        Krotka zawierająca wynik wyrównania i dwa wyrównane ciągi
    """
    def substitute(a,b):
        return mismatch_score if a != b else match_score
    
    n, m = len(s1), len(s2)

    if n == 0 and m == 0:
        return 0, s1, s2
    if n == 0:
        return gap_penalty * m, '-' * m, s2
    if m == 0:
        return gap_penalty * n, s1, '-' * n
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            ins = DP[i][j-1] + gap_penalty
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + gap_penalty

            DP[i][j] = max(ins, sub, delete)

    result_s1 = ""
    result_s2 = ""
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            current = DP[i][j]
            ins = DP[i][j-1] + gap_penalty
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + gap_penalty

            if current == sub:
                result_s1 = s1[i-1] + result_s1
                result_s2 = s2[j-1] + result_s2
                i -= 1
                j -= 1
            elif current == delete:
                result_s1 = s1[i-1] + result_s1
                result_s2 = "-" + result_s2
                i -= 1
            else:
                result_s1 = "-" + result_s1
                result_s2 = s2[j-1] + result_s2
                j -= 1
        elif i > 0:
            result_s1 = s1[i-1] + result_s1
            result_s2 = "-" + result_s2
            i -= 1
        else:
            result_s1 = "-" + result_s1
            result_s2 = s2[j-1] + result_s2
            j -= 1

    return DP[-1][-1], result_s1, result_s2

def allison_local_alignment(s1: str, s2: str,
                          match_score: int = 2,
                          mismatch_score: int = -1,
                          gap_penalty: int = -1) -> tuple[int, str, str, int, int]:
    """
    Znajduje optymalne lokalne wyrównanie (podobnie do algorytmu Smith-Waterman).

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków
        match_score: Punkty za dopasowanie
        mismatch_score: Punkty za niedopasowanie
        gap_penalty: Kara za lukę

    Returns:
        Krotka zawierająca wynik wyrównania, dwa wyrównane ciągi oraz pozycje początku
    """

    def substitute(a,b):
        return mismatch_score if a != b else match_score
    
    n, m = len(s1), len(s2)
    
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]
    traceback = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    max_score = 0
    max_pos = (0,0)

    for i in range(1,n+1):
        for j in range(1,m+1):
            ins = DP[i][j-1] + gap_penalty
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + gap_penalty

            DP[i][j] = max(0, ins, sub, delete)
            if DP[i][j] == sub:
                traceback[i][j] = (i - 1, j - 1)
            elif DP[i][j] == delete:
                traceback[i][j] = (i - 1, j)
            elif DP[i][j] == ins:
                traceback[i][j] = (i, j - 1)

            if DP[i][j] > max_score:
                max_score = DP[i][j]
                max_pos = (i, j)

    result_s1 = ""
    result_s2 = ""
    i, j = max_pos

    while DP[i][j] != 0:
        prev = traceback[i][j]
        if prev is None: break
        prev_i, prev_j = prev

        if prev_i == i-1 and prev_j == j-1:
            result_s1 = s1[i-1] + result_s1
            result_s2 = s2[j-1] + result_s2

        elif prev_i == i-1 and prev_j == j:
            result_s1 = s1[i-1] + result_s1
            result_s2 = "-" + result_s2

        else:
            result_s1 = "-" + result_s1
            result_s2 = s2[j-1] + result_s2
        i, j = prev_i, prev_j

    return max_score, result_s1, result_s2, i, j