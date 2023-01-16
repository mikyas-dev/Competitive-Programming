class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = ""
        words.sort(key = lambda x:x[-1])
        for i in range(len(words)):
            ans=ans+words[i][:-1]+" "
        return ans[:-1]
