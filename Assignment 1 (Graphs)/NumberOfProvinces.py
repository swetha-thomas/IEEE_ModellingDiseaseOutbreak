class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
       
        if not isConnected:
            return 0
        
        n = len(isConnected)
        visit = [False]*n
        
        def dfs(u):
            for v in range(n):
            #If there is a connection between u and v and v hasn't been visited yet, mark it as visited and repeat the same for v
                if isConnected[u][v] ==1 and visit[v] == False:
                    visit[v] = True
                    dfs(v)
        
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1 
                visit[i] = True
                dfs(i) # All vertices in a component get marked as visited
        
        return count
