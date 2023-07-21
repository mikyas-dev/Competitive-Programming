t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    chessboard = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0
    for i in range(n):
        for j in range(m):
            diagonal_sum = chessboard[i][j]
            for d in range(1, min(n, m)):
                if i + d < n and j + d < m:
                    diagonal_sum += chessboard[i + d][j + d]
                if i - d >= 0 and j - d >= 0:
                    diagonal_sum += chessboard[i - d][j - d]
                if i + d < n and j - d >= 0:
                    diagonal_sum += chessboard[i + d][j - d]
                if i - d >= 0 and j + d < m:
                    diagonal_sum += chessboard[i - d][j + d]
            max_sum = max(max_sum, diagonal_sum)
    
    print(max_sum)
