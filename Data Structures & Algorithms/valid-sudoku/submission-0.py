from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        three = defaultdict(set)
        for i in range(0, len(board)):
            rows = set()
            cols = set()
            for j in range(0, len(board)):
                if board[i][j] != ".":
                    if board[i][j] not in rows:
                        rows.add(board[i][j])
                    else:
                        return False
                    box = (i//3, j//3) # this is the set that represents THIS box
                    if board[i][j] not in three[box]:
                        three[box].add(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in cols:
                        cols.add(board[j][i])
                    else:
                        return False
                    
                    
            print(i)
            print(f'rows: {rows}')

        return True
