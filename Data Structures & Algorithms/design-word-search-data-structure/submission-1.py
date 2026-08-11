from typing import Optional


class TrieNode:
    def __init__(self):
        self._children: list[Optional["TrieNode"]] = [None] * 26
        self._is_end = False

    def get_child(self, char: str) -> Optional["TrieNode"]:
        index = ord(char) - ord("a")
        return self._children[index]

    def get_or_create_child(self, char: str) -> "TrieNode":
        index = ord(char) - ord("a")

        if self._children[index] is None:
            self._children[index] = TrieNode()

        return self._children[index]

    def set_end(self) -> None:
        self._is_end = True

    def is_end(self) -> bool:
        return self._is_end

    def children(self):
        return self._children


class WordDictionary:
    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self._root

        for char in word:
            node = node.get_or_create_child(char)

        node.set_end()

    def search(self, word: str) -> bool:
        return self._search(self._root, word, 0)

    def _search(
        self,
        node: TrieNode,
        word: str,
        index: int,
    ) -> bool:

        # Entire word consumed.
        if index == len(word):
            return node.is_end()

        char = word[index]

        # Normal character → one possible path.
        if char != ".":
            child = node.get_child(char)

            if child is None:
                return False

            return self._search(child, word, index + 1)

        # Wildcard → potentially 26 possible paths.
        for child in node.children():
            if child is not None:
                if self._search(child, word, index + 1):
                    return True

        return False