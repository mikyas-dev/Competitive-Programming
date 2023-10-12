class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        node = self.root
        xor_result = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite_bit = 1 - bit
            if opposite_bit in node.children:
                xor_result |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return xor_result
class Solution:
    def findMaximumXOR(self,nums):
        trie = Trie()
        max_xor = 0

        # Insert all numbers into the trie
        for num in nums:
            trie.insert(num)

        # Find maximum XOR for each number
        for num in nums:
            max_xor = max(max_xor, trie.find_max_xor(num))

        return max_xor
