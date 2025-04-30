def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Oblicza odległość Levenshteina między dwoma ciągami znaków.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Odległość Levenshteina (minimalna liczba operacji wstawienia, usunięcia
        lub zamiany znaku potrzebnych do przekształcenia s1 w s2)
    """
    # TODO: Zaimplementuj obliczanie odległości Levenshteina
    # TODO: Obsłuż przypadki brzegowe (puste ciągi)
    # TODO: Zaimplementuj algorytm dynamicznego programowania do obliczenia odległości
    n, m = len(s1), len(s2)
    if n == m == 0: return 0
    DP = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,m+1):
        DP[0][i] = i
    
    for i in range(1,n+1):
        DP[i][0] = i
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1            
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + cost
    
    return DP[-1][-1]