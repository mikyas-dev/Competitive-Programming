class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        n = len(words)
        correct=""
        for i in range(0,n-1):
            min=i
            for j in range(i+1,n):
                if words[j][len(words[j])-1]<words[min][len(words[min])-1]:
                    min = j
            if min !=i:
                words[min],words[i]=words[i],words[min]
        for x in range(0,n):
            if x == n-1:
                correct=correct+words[x][0:len(words[x])-1]
            else:
                correct=correct+words[x][0:len(words[x])-1]+" "
        return correct
        
