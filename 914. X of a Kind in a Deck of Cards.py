class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
            
        counter = Counter(deck)
        value  = sorted(counter.values())
        maxima = value[0]

        for val in value:
            temp = gcd(val,maxima)
            if maxima == 1 or temp == 1 :
                return False
            maxima = temp
        return True
