class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        def recu(x: int):
            if x%3==0 and x!=3:
                return recu(x/3)
            elif x%3!=0:
                return False
            if x==3:  
                return True
            
        return recu(n) if n!=1 else True
      
    
