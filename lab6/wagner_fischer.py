def wagner_fischer(s1: str, s2: str,
                  insert_cost: int = 1,
                  delete_cost: int = 1,
                  substitute_cost: int = 1) -> int:
    """
    Oblicza odległość edycyjną używając algorytmu Wagnera-Fischera (programowanie dynamiczne).

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków
        insert_cost: Koszt operacji wstawienia
        delete_cost: Koszt operacji usunięcia
        substitute_cost: Koszt operacji zamiany

    Returns:
        Odległość edycyjna z uwzględnieniem kosztów operacji
    """

    def substitute(a,b):
        return substitute_cost if a != b else 0
    
    n, m = len(s1), len(s2)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,m+1):
        DP[0][i] = i

    for i in range(1,n+1):
        DP[i][0] = i
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            ins = DP[i][j-1] + insert_cost
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + delete_cost
            DP[i][j] = min(ins, sub, delete)
        
    return DP[-1][-1]

def wagner_fischer_with_alignment(s1: str, s2: str) -> tuple[int, str, str]:
    """
    Oblicza odległość edycyjną i zwraca wyrównanie sekwencji.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Krotka zawierająca odległość edycyjną i dwa wyrównane ciągi
        (w wyrównanych ciągach '-' oznacza lukę)
    """
    def substitute(a,b):
        return 1 if a != b else 0
    
    n, m = len(s1), len(s2)
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,m+1):
        DP[0][i] = i

    for i in range(1,n+1):
        DP[i][0] = i

    for i in range(1,n+1):
        for j in range(1,m+1):
            ins = DP[i][j-1] + 1
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + 1

            DP[i][j] = min(ins, sub, delete)

    result_s1 = ""
    result_s2 = ""
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            current = DP[i][j]
            ins = DP[i][j-1] + 1
            sub = substitute(s1[i-1], s2[j-1]) + DP[i-1][j-1]
            delete = DP[i-1][j] + 1

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

def wagner_fischer_space_optimized(s1: str, s2: str) -> int:
    """
    Oblicza odległość edycyjną używając zoptymalizowanej pamięciowo wersji algorytmu.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Odległość edycyjna
    """
    def substitute(a,b):
        return 1 if a != b else 0
    
    n, m = len(s1), len(s2)
    k = min(n,m)
    r = max(n,m)
    DP = [[0 for _ in range(k+1)] for _ in range(2)]

    filled_row = 0
    not_filled_row = 1

    for i in range(1,k+1):
        DP[filled_row][i] = i
    
    for i in range(1,r+1):
        DP[not_filled_row][0] = i

        for j in range(1,k+1):
            sub_cost = substitute(s1[i-1], s2[j-1]) if r == n else substitute(s2[i-1], s1[j-1])
            ins = DP[not_filled_row][j-1] + 1
            sub = sub_cost + DP[filled_row][j-1]
            delete = DP[filled_row][j] + 1
            DP[not_filled_row][j] = min(ins, sub, delete)
        
        filled_row, not_filled_row = not_filled_row, filled_row
    return DP[filled_row][-1]