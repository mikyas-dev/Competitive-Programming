class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ''.join(ch for ch in s if ch.isalnum()).lower()
        return snew[::-1]==snew
