class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      parent = [i for i in range(len(edges) + 1)]

      def find(x): # Finding the root parent of x
          if x != parent[x]:
              parent[x] = find(parent[x])
          return parent[x]

      def union(x, y):
          parent[find(y)] = find(x)   # Make the root parent of y = root parent of x (Single component)

      for a, b in edges:
          if find(a) == find(b):  # If a and b have same root parent, then path between a and b is redundant
              return [a, b]
          else:
              union(a, b)

