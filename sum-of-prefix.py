class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.val = 0
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
            current_node.val += 1
        current_node.is_word = True
        
    def search(self, word):
        curr= self.root
        res = 0
        for char in word:
            curr = curr.children[char]
            res += curr.val

        return res
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = WordDictionary()
        for word in words:
            trie.addWord(word)

        ans = []
        for word in words:
            ans.append(trie.search(word))

        return ans
