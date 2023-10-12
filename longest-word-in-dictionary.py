class TriesNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class Tries:
    def __init__(self) -> None:
        self.root = TriesNode()
        self.words = ""
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TriesNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children or not current.children[char].is_word:
                return False
            current = current.children[char]
        return current.is_word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        tries = Tries()
        result = ""
        for word in words:
            tries.insert(word)
            if tries.search(word):
                if len(word) > len(result) or (word < result and len(word) == len(result)):
                    result = word
    
        return result
            
        
