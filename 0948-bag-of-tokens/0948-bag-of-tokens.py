class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans=score=0
        i,j=0,len(tokens)-1
        while i<=j:
            if score<0:
                break
            if power<tokens[i]:
                power+=tokens[j]
                j-=1
                score-=1
                continue
            score+=1
            ans=max(ans,score)
            power-=tokens[i]
            i+=1
        return ans