import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
visited = [False] * N
todo = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    todo[b-1].append(a-1)

X = int(input())
visited[X-1] = True
ans = 0
stack = todo[X-1][:]

while stack:
    now = stack.pop()
    if not visited[now]:
        ans += 1
        visited[now] = True
        for do in todo[now]:
            if not visited[do]:
                stack.append(do)

print(ans)