import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
a, b = map(int, input().split())
M = int(input())
tree = [set() for _ in range(N + 1)]
visited = [-1] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    tree[x].add(y)
    tree[y].add(x)


visited[a] = 0


def bfs(c, d):
    q = deque([c])

    while q:
        now = q.popleft()
        for togo in tree[now]:
            if visited[togo] == -1:
                q.append(togo)
                visited[togo] = visited[now] + 1
                if togo == d:
                    return
    return


bfs(a, b)
print(visited[b])