class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                piece = board[r][c]
                box_index = (r//3, c//3)

                if piece == '.': continue
                if piece in rows[r] or piece in columns[c] or piece in boxes[box_index]: return False

                rows[r].add(piece)
                columns[c].add(piece)
                boxes[box_index].add(piece)
        return True