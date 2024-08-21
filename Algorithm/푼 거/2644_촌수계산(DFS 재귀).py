import sys
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


def dfs(s):
    for togo in tree[s]:
        if visited[togo] == -1:
            visited[togo] = visited[s] + 1
            dfs(togo)

            
dfs(a)
print(visited[b])
