class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0   # count of number of fresh oranges
        rotten = deque([])  # queue that keeps track of rotten oranges
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # if fresh
                    fresh += 1
                elif grid[i][j] == 2:   # if rotten
                    rotten.append((i, j))
        
        if fresh == 0:
            return 0
        
        def bfs(q, ans, fresh):
            while q:
                lenq = len(q)
                for i in range(lenq):
                    i, j = q.popleft()
                    
                    # 4-directionally adjacent cells to a rotten orange
                    for step_x, step_y in ((0, 1), (0, -1), (-1, 0), (1, 0)):  
                        x = step_x + i
                        y = step_y + j
                        
                        # if adjacent cell is within grid and fresh
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1: 
                            grid[x][y] = 2  # update to rotten
                            # decrement number of fresh oranges by 1
                            fresh -= 1  
                            # enqueue new rotten orange
                            q.append((x, y))    
                
                ans += 1 # keeps track of minutes
            
            # if no fresh oranges left, return ans else return -1
            return -1 if fresh else ans    
        
        return bfs(rotten, -1, fresh)
