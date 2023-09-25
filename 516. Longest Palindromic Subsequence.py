class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Create a 2D table to store the results of subproblems
        dp = [[0] * n for _ in range(n)]

        # Initialize the diagonal elements to 1 because each character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill in the table in a bottom-up manner
        for len_subseq in range(2, n + 1):
            for i in range(n - len_subseq + 1):
                j = i + len_subseq - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The result is stored in the top-right corner of the table
        return dp[0][n - 1]

