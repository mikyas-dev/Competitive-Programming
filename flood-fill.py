class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

        def isbound( row, col):
            return (0 <= row < len(image)) and (0 <= col < len(image[0]))
        
        def dfs(row ,col):
            prev = image[row][col]
            image[row][col] = color
            
            visited[row][col] = True

            for row_change, col_change in direction:
                new_row = row + row_change
                new_col = col + col_change

                if isbound(new_row,new_col) and not visited[new_row][new_col] and image[new_row][new_col] == prev:
                    dfs(new_row,new_col)
                
        if image[sr][sc] != color:
            dfs(sr,sc)
        return image


        return []