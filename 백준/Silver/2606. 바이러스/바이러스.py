import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[False]*(N+1) for _ in range(N+1)]


for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False]*(N+1)



def dfs(node):
    visited1[node] = True
    for i in range(1, N + 1):
        if not visited1[i] and graph[node][i]:
            dfs(i)

dfs(1)
c = sum([1 for i in visited1 if i == 1])-1
print(c)
