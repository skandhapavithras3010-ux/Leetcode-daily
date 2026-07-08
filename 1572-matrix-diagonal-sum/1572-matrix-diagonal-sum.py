class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0

        for i in range(len(mat)):
            sum += mat[i][i]  # Main Diagonal
            sum += mat[i][len(mat)-1-i] # Secondary Diagonal

        if len(mat) % 2 == 1:
            sum -= mat[len(mat)//2][len(mat)//2]
        return sum