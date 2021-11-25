class Solution(object):
    def allPathsSourceTarget(self, graph):
        fullpath = []
        n = len(graph)
        
        for v in graph[0]:
            arr = [0, v]   # inlcudes second vertex (v) in path from vertex 0
            self.dfs(v, graph, n, arr, fullpath)
        return fullpath
    
    def dfs(self, v, graph, n, arr, fullpath):
        if v == n-1:   # if last vertex has been reached
            fullpath.append(list(arr))  # appends complete path to list of paths
            return
        for node in graph[v]:  # iterates through each vertex (node) connected to vertex v
            arr.append(node)
            self.dfs(node, graph, n, arr, fullpath) # finds path through 0->v->node
            arr.pop()
