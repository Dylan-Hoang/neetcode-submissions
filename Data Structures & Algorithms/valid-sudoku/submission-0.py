class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set)
        columndict = defaultdict(set)
        squaredict = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                if num in rowdict[r]:
                    return False
                rowdict[r].add(num)
                if num in columndict[c]:
                    return False
                columndict[c].add(num)
                if num in squaredict[(r//3,c//3)]:
                    return False
                squaredict[(r//3,c//3)].add(num)
        return True
            

                
        