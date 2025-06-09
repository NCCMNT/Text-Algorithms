def naive_edit_distance(s1: str, s2: str) -> int:
    """
    Oblicza odległość edycyjną między dwoma ciągami używając naiwnego algorytmu rekurencyjnego.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Odległość edycyjna (minimalna liczba operacji wstawienia, usunięcia
        lub zamiany znaku potrzebnych do przekształcenia s1 w s2)
    """
    n, m = len(s1), len(s2)
    if n == 0: return m
    if m == 0: return n
    if s1[0] == s2[0]:
        return naive_edit_distance(s1[1:], s2[1:])
    
    return 1 + min(
        naive_edit_distance(s1, s2[1:]),
        naive_edit_distance(s1[1:], s2[1:]),
        naive_edit_distance(s1[1:], s2)
    )

def naive_edit_distance_with_operations(s1: str, s2: str) -> tuple[int, list[str]]:
    """
    Oblicza odległość edycyjną i zwraca listę operacji potrzebnych do przekształcenia s1 w s2.

    Args:
        s1: Pierwszy ciąg znaków
        s2: Drugi ciąg znaków

    Returns:
        Krotka zawierająca odległość edycyjną i listę operacji
        Operacje: "INSERT x", "DELETE x", "REPLACE x->y", "MATCH x"
    """
    n, m = len(s1), len(s2)
    if n == 0 and m == 0: return (0, [])
    if n == 0:
        dist, op = naive_edit_distance_with_operations(s1, s2[1:])
        return (dist + 1, [f"INSERT {s2[0]}"] + op)
    if m == 0:
        dist, op = naive_edit_distance_with_operations(s1[1:], s2)
        return (dist + 1, [f"INSERT {s1[0]}"] + op)
    if s1[0] == s2[0]:
        match, mat_op = naive_edit_distance_with_operations(s1[1:], s2[1:])
        return (match, [f"MATCH {s1[0]}"] + mat_op) 
    
    insert, ins_op = naive_edit_distance_with_operations(s1, s2[1:])
    substitute, sub_op = naive_edit_distance_with_operations(s1[1:], s2[1:])
    delete, del_op = naive_edit_distance_with_operations(s1[1:], s2)

    mini = min(insert, substitute, delete)
    if insert == mini:
        return (1 + insert, [f"INSERT {s2[1]}"] + ins_op)
    elif substitute == mini:
        return (1 + substitute, [f"REPLACE {s1[0]}->{s2[0]}"] + sub_op)
    else:
        return (1 + delete, [f"DELETE {s1[1]}"] + del_op)