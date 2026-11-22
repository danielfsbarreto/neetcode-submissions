class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        # picking the right row
        p1, p2 = 0, rows - 1
        while p1 <= p2:
            row = (p1 + p2) // 2
            if target > matrix[row][-1]:
                p1 = row + 1
            elif target < matrix[row][0]:
                p2 = row - 1
            else:
                break

        # binary search on the selected row
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False
        
