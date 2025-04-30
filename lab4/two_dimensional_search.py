def find_pattern_in_column(text_column: str, pattern_columns: list[str]) -> list[tuple[int, int]]:
    """
    Wyszukuje wszystkie kolumny wzorca w kolumnie tekstu.

    Args:
        text_column: Kolumna tekstu
        pattern_columns: Lista kolumn wzorca

    Returns:
        Lista krotek (pozycja, indeks kolumny), gdzie znaleziono kolumnę wzorca
    """
    # TODO: Zaimplementuj wyszukiwanie kolumn wzorca w kolumnie tekstu
    # TODO: Dla każdej kolumny wzorca, przeszukaj kolumnę tekstu
    # TODO: Zwróć listę krotek (pozycja, indeks kolumny) dla znalezionych dopasowań
    n = len(text_column)
    if n == 0 or len(pattern_columns) == 0: return []
    results = []
    
    for j, pcol in enumerate(pattern_columns):
        m = len(pcol)
        if m > n: continue
        for i in range(n - m + 1):
            if pcol == text_column[i:i+m]:
                results.append((i, j))

    return results


def find_pattern_2d(text: list[str], pattern: list[str]) -> list[tuple[int, int]]:
    """
    Wyszukuje wzorzec dwuwymiarowy w tekście dwuwymiarowym.

    Args:
        text: Tekst dwuwymiarowy (lista ciągów znaków tej samej długości)
        pattern: Wzorzec dwuwymiarowy (lista ciągów znaków tej samej długości)

    Returns:
        Lista krotek (i, j), gdzie (i, j) to współrzędne lewego górnego rogu wzorca w tekście
    """
    # TODO: Zaimplementuj wyszukiwanie wzorca dwuwymiarowego
    # TODO: Obsłuż przypadki brzegowe (pusty tekst/wzorzec, wymiary)
    # TODO: Sprawdź, czy wszystkie wiersze mają taką samą długość
    # TODO: Zaimplementuj algorytm wyszukiwania dwuwymiarowego
    # TODO: Zwróć listę współrzędnych lewego górnego rogu dopasowanego wzorca
    a, b = len(text), len(pattern)
    if a == 0 or b == 0: return []

    c, d = len(text[0]), len(pattern[0])
    if d > c or b > a: return []

    if any(len(line) != d for line in pattern) or any(len(line) != c for line in text): return []
    results = []
    pattern_cols = list(''.join(x) for x in zip(*pattern))
    S = set()

    for i in range(c):
        text_col = ''.join([text[j][i] for j in range(a)])
        found = find_pattern_in_column(text_col, pattern_cols)
        for row, num in found:
            S.add((row, i, num))

    for i in range(a):
        for j in range(c - d + 1):
            flag = True
            for m in range(d):
                if (i,j+m,m) not in S:
                    flag = False
                    break
            if flag:
                results.append((i,j))

    return results