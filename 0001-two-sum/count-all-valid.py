class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        num = math.factorial(n*2)
        dem = 2 ** n
        return (num//dem % MOD )      
