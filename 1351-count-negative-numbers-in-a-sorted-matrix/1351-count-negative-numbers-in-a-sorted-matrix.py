class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        i = 0
        j = n - 1

        while i < m and j >= 0:
            if grid[i][j] < 0:
                count += m - i
                j -= 1
            else:
                i += 1
        return count

