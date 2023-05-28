class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def prime_sieve(n):
            is_prime = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i <= n:
                if is_prime[i]:
                    j = 2 * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime
        
        ans = []
        temp = prime_sieve(right)
        
        for i in range(left,right+1):
            if temp[i]:
                ans.append(i)

        if len(ans)<2:
            return [-1,-1]
        
        minIdx = 0
        diff = right - left
        for i in range(len(ans)-1):
            if ans[i+1] - ans[i] < diff:
                diff = ans[i+1] - ans[i]
                minIdx = i

            
        
        return ans[minIdx:minIdx+2]