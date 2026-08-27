class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                # if val in rows[r] or val in cols[c] or val in squares[r//3, c//3]:
                if val in rows[r]:
                    print("Value: " + val)
                    print(rows)
                    return False
                if val in cols[c]:
                    print("Value: " + val)
                    print("cols")
                    print(cols)
                    return False
                if val in squares[r//3, c//3]:
                    print("Value: " + val)
                    print(squares[r//3, c//3])
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[r//3, c//3].add(val)
        return True