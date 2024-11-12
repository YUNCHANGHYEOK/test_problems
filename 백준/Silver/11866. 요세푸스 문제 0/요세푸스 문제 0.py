from collections import deque

N, M = map(int, input().split())
list = [i for i in range(1, N+1)]
dq = deque(list)

result = []
while len(dq) > 0:
    dq.rotate(-(M-1))
    result.append(dq.popleft())

print('<'+', '.join(map(str, result))+'>')