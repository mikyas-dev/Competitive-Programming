class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.words = {}
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        temp = val
        if key in self.words:
            val -= self.words[key]
        self.words[key] = temp
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.value += val
        current.is_word = True
        

    def sum(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]
        return current.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
