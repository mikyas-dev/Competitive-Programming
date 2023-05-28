class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(index):
            if index == n + 1:
                self.count += 1
                return
            for i in range(1, n + 1):
                if not visited[i] and (index % i == 0 or i % index == 0):
                    visited[i] = True
                    backtrack(index + 1)
                    visited[i] = False

        visited = [False] * (n + 1)
        self.count = 0
        backtrack(1)
        return self.count