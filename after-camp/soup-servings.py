class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:  # If n is larger, the probability approaches 1
            return 1.0

        memo = {}

        def serve(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5  # Half probability if both are empty

            if a <= 0:
                return 1.0  # Probability 1 if A is empty first

            if b <= 0:
                return 0.0  # Probability 0 if B is empty first

            prob = 0.25 * (
                serve(a - 100, b) +
                serve(a - 75, b - 25) +
                serve(a - 50, b - 50) +
                serve(a - 25, b - 75)
            )

            memo[(a, b)] = prob
            return prob

        return serve(n, n)

