class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):

                value = board[r][c]
                box_index = (int(r/3),int(c/3))
                if value == ".":
                    continue
                if value in rows[r] or value in columns[c] or value in boxes[box_index]:
                    return False
                
                rows[r].add(value)
                columns[c].add(value)
                boxes[box_index].add(value)

        return True
