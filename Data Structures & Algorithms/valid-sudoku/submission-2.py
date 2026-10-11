class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_row = [set([]) for _ in range(9)]
        valid_col = [set([]) for _ in range(9)]
        valid_square = [set([]) for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                curr = board[i][j]
                if curr.isnumeric():
                    if curr not in valid_row[j]:
                        valid_row[j].add(curr)
                    else:
                        return False
                    
                    if curr not in valid_col[i]:
                        valid_col[i].add(curr)
                    else:
                        return False

                    if curr not in valid_square[i // 3 * 3 + j // 3]:
                        valid_square[i // 3 * 3 + j // 3].add(curr)
                    else:
                        return False
        
        return True