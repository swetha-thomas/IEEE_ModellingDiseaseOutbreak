nm = input().split()
n, m = int(nm[0]), int(nm[1])
edges = []
parent = [i for i in range(m + 1)]
for i in range(m):
    a_b_w = input().split()
    w, a, b = int(a_b_w[2]), int(a_b_w[0]), int(a_b_w[1])
    edges.append((w, a, b))

    edges.sort()

def find(x):  # Finding the root parent of x
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(y)] = find(x)  # Make the root parent of y = root parent of x (Single component)


cost = 0
for edge in edges:
    if find(edge[1]) != find(edge[2]):
        union(edge[1], edge[2])
        cost += edge[0]

print(cost)
