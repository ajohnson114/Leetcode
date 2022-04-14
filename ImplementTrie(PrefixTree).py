class Trie:
  """
  Relatively simple, we just have to be mindful of the edge case where the word is bigger than the one we're hoping to see that it starts with
  """
    def __init__(self):
        self.trie = []

    def insert(self, word: str) -> None:
        self.trie.append(word)

    def search(self, word: str) -> bool:
        for i in self.trie:
            if word == i:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        x = len(prefix)
        for i in self.trie:
            if x > len(i):
                continue
            if i[0:x] == prefix:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
