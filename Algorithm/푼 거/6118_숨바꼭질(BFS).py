import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = {i: set() for i in range(1, N+1)}
visited = [False] * (N+1)
visited[1] = True
# 번호, 거리, 개수
ans = [0, 0, 0]

for _ in range(M):
    S, E = map(int, input().split())
    grid[S].add(E)
    grid[E].add(S)

q = deque([[1, 0]])
while q:
    n, d = q.popleft()

    for togo in grid[n]:
        # 아직 안 가봤다면
        if not visited[togo]:
            visited[togo] = True
            q.append([togo, d+1])
            if ans[1] < d+1:
                ans = [togo, d+1, 1]
            elif ans[1] == d+1:
                ans[2] += 1
                if ans[0] > togo:
                    ans[0] = togo

print(*ans)