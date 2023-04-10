class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = set()
            for j in range(9):
                
                if board[i][j].isnumeric():
                    if board[i][j] in check:
                        return False
                    check.add(board[i][j])
            
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i].isnumeric():
                    if board[j][i] in check:
                        return False
                    check.add(board[j][i])
            
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        num = board[row][col]
                        if num != '.':
                            if num in box_set:
                                return False
                            box_set.add(num)

        return True