class PrefixTree:
    def __init__(self):
        self.children: dict[str, PrefixTree] = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = PrefixTree()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True
