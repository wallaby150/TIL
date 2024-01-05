import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
fs = [[] for _ in range(N + 1)]
best = [50, []]

while True:
    A, B = map(int, input().split())
    if A == B == -1:
        break
    fs[A].append(B)
    fs[B].append(A)

for idx in range(1, N+1):
    visited = [False] * (N + 1)
    visited[0] = True
    visited[idx] = True

    q = deque([])
    for mem in fs[idx]:
        q.append((1, mem))
        visited[mem] = True
    far = 1

    while q:
        now_far, mem = q.popleft()
        far = max(now_far, far)

        for togo in fs[mem]:
            if visited[togo] == False:
                q.append((now_far + 1, togo))
                visited[togo] = True

    if far < best[0]:
        best = [far, [idx]]
    elif far == best[0]:
        best[1].append(idx)


print(best[0], len(best[1]))
print(*best[1])