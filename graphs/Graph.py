from collections import defaultdict
from collections import deque

n=8
a=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
m=[]
for i in range(n):
    m.append([0]*n)
for u, v in a:
    m[u][v]=1
    # m[v][u]=1 undirected

# adjacency list
d= defaultdict(list)

for u,v in a:
    d[u].append(v)

# DFS with recursion with o(v+e)

# def dfs_recursive(node):
#     print(node)
#     for neighbour_node in D[node]:
#         if neighbour_node not in seen:
#             seen.add(neighbour_node)
#             dfs_recursive(neighbour_node)
# source =0
# seen=set()
# seen.add(source)
# dfs_recursive(source)

# DFS using stack iterative

source =0
seen=set()
seen.add(source)
stack=[source]

while stack:
    node=stack.pop()
    print(node) 
    for neighbour in d[source]:
        if neighbour not in seen:
            seen.add(neighbour)
            stack.append(neighbour)


# BFS using queue
source=0
seen= set()
seen.add(source)
q=deque()
q.append(source)
while stack:
    node=q.popleft()
    print(node) 
    for neighbour in d[source]:
        if neighbour not in seen:
            seen.add(neighbour)
            stack.append(neighbour)


