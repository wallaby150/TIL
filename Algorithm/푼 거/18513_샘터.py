import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
spring = list(map(int, input().split()))
ans = cnt = 0
q = deque([])
visited = set()

for s in spring:
    q.append([0, s])
    visited.add(s)

while q:
    far, now = q.popleft()
    for togo in [now-1, now+1]:
        if togo not in visited:
            ans += far + 1
            cnt += 1
            visited.add(togo)
            q.append([far+1, togo])

            if cnt == K:
                break
    else:
        continue
    break

print(ans)
