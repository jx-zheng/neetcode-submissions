class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total_cells = rows * cols

        l, r = 0, total_cells - 1

        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            l_row = l // cols
            l_col = l % cols
            r_row = r // cols
            r_col = r % cols

            print(mid_row)
            print(f"a {mid}")
            if matrix[mid_row][mid_col] == target:
                return True
            
            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1


        return False
