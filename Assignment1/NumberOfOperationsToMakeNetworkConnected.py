class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: # not enough cables
            return -1
        G = [set() for i in range(n)]   # adjacency list
        for i, j in connections:
            G[i].add(j) 
            G[j].add(i)
        seen = [0] * n

        def dfs(i):
            if seen[i]: #if a vertex has already been seen before then it is part of an already visited component
                return 0
            seen[i] = 1
            for j in G[i]: 
                dfs(j) 
            return 1 # 1 is returned if vertex passed as parameter is part of a new component

        return sum(dfs(i) for i in range(n)) - 1 # the sum returns number of components
