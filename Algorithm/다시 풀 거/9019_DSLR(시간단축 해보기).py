import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    q = deque([[A, '']])

    while q:
        now, com = q.popleft()
        if now == B:
            print(com)
            break

        d = now * 2 % 10000
        if visited[d] == 0:
            visited[d] = 1
            q.append([d, com + 'D'])

        s = 9999 if now == 0 else now - 1
        if visited[s] == 0:
            visited[d] = 1
            q.append([s, com + 'S'])

        l = (now % 1000) * 10 + now // 1000
        if visited[l] == 0:
            visited[l] = 1
            q.append([l, com + 'L'])

        r = (now % 10) * 1000 + now // 10
        if visited[r] == 0:
            visited[r] = 1
            q.append([r, com + 'R'])

