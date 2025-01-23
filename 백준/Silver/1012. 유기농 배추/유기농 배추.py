import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        input_x, input_y = map(int, input().split())
        graph[input_x][input_y] = 1
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[x][y] = 0  # 수정: 방문한 배추를 0으로 표시하여 중복 방지
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0  # 수정: 연결된 배추도 방문 처리
                
    count = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    
    answer.append(count)
print('\n'.join(map(str,answer)))
    

            
                
            