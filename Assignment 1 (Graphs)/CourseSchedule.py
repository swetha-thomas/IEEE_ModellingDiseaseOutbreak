class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        graph = collections.defaultdict(set) # directed graph 
        for course, pre in prerequisites:
            graph[pre].add(course) # set a directed edge 

        def dfs(x):
            visited[x] = -1     # currently visiting path
            for y in graph[x]:
                if visited[y] == -1 or (visited[y] == 0 and not dfs(y)):    # if cycle is encountered 
                    return False
            visited[x] = 1  # all vertices in path starting from x have been visited
            return True

        for i in range(numCourses):
            if visited[i] == 0 and not dfs(i): # check if cycle is not present (DAG)
                return False
        return True
