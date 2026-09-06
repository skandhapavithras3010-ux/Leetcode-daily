from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        answer = [[-1]*n for _ in range(m)]
        
        queue = deque()
         
         # Put all the 0's in queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    queue.append((i,j))

        # BFS
        while queue:
            i,j = queue.popleft()
            directions = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            
            for x,y in directions:
                # Chech if neighbour is inside the matrix
                if (0<=x<m) and (0<=y<n):
                    # Check if neighbour hasnt been visited
                    if answer[x][y] == -1:
                        # Neighbour is one step farther
                        answer[x][y] = answer[i][j] + 1
                        # Add neighbour to queue
                        queue.append((x,y))
        return answer

