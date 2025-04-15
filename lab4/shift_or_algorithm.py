def set_nth_bit(n: int) -> int:
    """
    Zwraca maskę bitową z ustawionym n-tym bitem na 1.

    Args:
        n: Pozycja bitu do ustawienia (0-indeksowana)

    Returns:
        Maska bitowa z n-tym bitem ustawionym na 1
    """
    # TODO: Zaimplementuj ustawianie n-tego bitu
    return 1 << n


def nth_bit(m: int, n: int) -> int:
    """
    Zwraca wartość n-tego bitu w masce m.

    Args:
        m: Maska bitowa
        n: Pozycja bitu do odczytania (0-indeksowana)

    Returns:
        Wartość n-tego bitu (0 lub 1)
    """
    # TODO: Zaimplementuj odczytywanie n-tego bitu
    return (m >> n) & 1


def make_mask(pattern: str) -> list:
    """
    Tworzy tablicę masek dla algorytmu Shift-Or.

    Args:
        pattern: Wzorzec do wyszukiwania

    Returns:
        Tablica 256 masek, gdzie każda maska odpowiada jednemu znakowi ASCII
    """
    # TODO: Zaimplementuj tworzenie tablicy masek dla algorytmu Shift-Or
    # TODO: Utwórz tablicę z maskami dla wszystkich znaków ASCII
    # TODO: Dla każdego znaku w pattern, ustaw odpowiednie bity w maskach
    if len(pattern) == 0: return []
    masks = [~0 for _ in range(256)]
    for i, c in enumerate(pattern):
        masks[ord(c)] &= ~(set_nth_bit(i))
    return masks


def shift_or(text: str, pattern: str) -> list[int]:
    """
    Implementacja algorytmu Shift-Or do wyszukiwania wzorca.

    Args:
        text: Tekst do przeszukania
        pattern: Wzorzec do wyszukiwania

    Returns:
        Lista pozycji (0-indeksowanych), na których znaleziono wzorzec
    """
    # TODO: Zaimplementuj algorytm Shift-Or
    # TODO: Obsłuż przypadki brzegowe (pusty wzorzec, wzorzec dłuższy niż tekst)
    # TODO: Utwórz maski dla wzorca
    # TODO: Zainicjalizuj stan początkowy
    # TODO: Zaimplementuj główną logikę algorytmu
    # TODO: Wykryj i zapisz pozycje dopasowań
    if len(text) == 0 or len(pattern) == 0 or len(pattern) > len(text): return []
    result = []
    masks = make_mask(pattern)
    s = ~0
    m = len(pattern)
    for i, c in enumerate(text):

        s = (s << 1) | masks[ord(c)]

        if nth_bit(s, m - 1) == 0:
            result.append(i - m + 1)

    return result

print(nth_bit((~0 << 1), 3))
print(nth_bit((~0 << 1), 2))
print(nth_bit((~0 << 1), 3))
print(nth_bit((~0 << 1), 0))