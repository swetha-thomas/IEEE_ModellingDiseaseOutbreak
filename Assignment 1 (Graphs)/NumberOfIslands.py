class Solution:
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':   
                    self.dfs(grid,i,j)
                    count =count + 1
        return count

    def dfs(self,grid,i,j):
        grid[i][j] = 0 
        for x_step, y__step in (1,0), (-1,0), (0,-1), (0,1): # checking 4 directionally adjacent cells for water
            x = i + x_step
            y = j + y_step
            if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1': # to check if there is adjacent land cells in an island
                self.dfs(grid,x,y)
