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


def dfs(c, d):
    stack = [c]

    while stack:
        now = stack.pop()
        for togo in tree[now]:
            if visited[togo] == -1:
                stack.append(togo)
                visited[togo] = visited[now] + 1
                if togo == d:
                    return
    return


dfs(a, b)
print(visited[b])