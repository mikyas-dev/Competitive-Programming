class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def isMagic(sub_grid):
            arr = []
            for i in range(len(sub_grid)):
                for j in range(len(sub_grid[0])):
                    arr.append(sub_grid[i][j])
            if sorted(arr) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                return False
            
            row_sums = [sum(r) for r in sub_grid]
            if len(set(row_sums)) > 1:
                return False

            col_sums = [sum([row[i] for row in sub_grid]) for i in range(3)]
            if len(set(col_sums)) > 1 and row_sums[0] != col_sums[0]:
                return False
            
            diag_sums = sum([sub_grid[i][i] for i in range(3)])
            return diag_sums == row_sums[0]

        res = 0
        for i in range(m-2):
            for j in range(n-2):
                sub_grid = [[grid[x][y] for y in range(j, j+3)] for x in range(i, i+3)]
                if(isMagic(sub_grid)):
                    res += 1
        return res