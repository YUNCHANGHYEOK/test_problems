import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘려줍니다.
N,M = map(int,input().split())

graph=[[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False]*(N+1)

cnt = 0
def dfs(node):
    visited1[node] = True
    for i in range(1, N + 1):
        if not visited1[i] and graph[node][i]:
            dfs(i)


# 모든 노드에 대해 DFS를 시작
for i in range(1, N + 1):
    if not visited1[i]:  # 방문하지 않은 노드에서 DFS 시작
        dfs(i)
        cnt += 1  # 새로운 연결 요소 발견 시 개수 증가


print(cnt)