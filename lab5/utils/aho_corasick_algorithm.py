from collections import deque
from typing import List, Tuple, Optional

class AhoCorasickNode:
    def __init__(self, char):
        # TODO: Zainicjalizuj struktury potrzebne dla węzła w drzewie Aho-Corasick
        self.char = char
        self.children = dict()
        self.fail_link = None
        self.outputs = []

class AhoCorasick:
    def __init__(self, patterns: List[str]):
        # TODO: Zainicjalizuj strukturę Aho-Corasick i usuń puste wzorce
        self.root = AhoCorasickNode(None)
        self.patterns = list(filter(lambda x: len(x) != 0, patterns))

    def _build_trie(self):
        """Builds the trie structure for the given patterns."""
        # TODO: Zaimplementuj budowanie drzewa typu trie dla podanych wzorców
        for pattern in self.patterns:

            node = self.root
            for c in pattern:

                if c not in node.children:
                    node.children[c] = AhoCorasickNode(c)

                node = node.children[c]
                
            node.outputs.append(pattern)

    def _build_failure_links(self):
        """Builds failure links and propagates outputs through them."""
        # TODO: Zaimplementuj tworzenie failure links
        # TODO: Utwórz kolejkę do przechodzenia przez drzewo w szerokość (BFS)
        # TODO: Zainicjalizuj łącza awaryjne dla węzłów na głębokości 1
        # TODO: Użyj BFS do ustawienia łączy awaryjnych dla głębszych węzłów
        # TODO: Propaguj wyjścia przez łącza awaryjne

        Q = deque([])

        for node in self.root.children.values():
            node.fail_link = self.root
            Q.append(node)

        while Q:
            node = Q.popleft()

            for c, child in node.children.items():
                fnode = node.fail_link
                
                while fnode is not None and c not in fnode.children:
                    fnode = fnode.fail_link

                child.fail_link = fnode.children[c] if fnode else self.root
                child.outputs += child.fail_link.outputs if child.fail_link else []
                Q.append(child)

    def search(self, text: str) -> Tuple[List[Tuple[int, str]], int]:
        """
        Searches for all occurrences of patterns in the given text.

        Returns:
            List of tuples (start_index, pattern).
        """
        # TODO: Zaimplementuj wyszukiwanie wzorców w tekście
        # TODO: Zwróć listę krotek (indeks_początkowy, wzorzec)
        if len(text) == 0: return [], 0
        results = []
        self._build_trie()
        self._build_failure_links()
        node = self.root
        compares = 0

        for i, c in enumerate(text):
            compares += 1
            while node is not None and c not in node.children:
                compares += 1
                node = node.fail_link

            if node is None:
                node = self.root
                continue
            node = node.children[c]

            for pattern in node.outputs:
                results.append((i - len(pattern) + 1, pattern))

        return results, compares