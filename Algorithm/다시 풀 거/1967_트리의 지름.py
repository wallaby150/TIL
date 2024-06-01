import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dfs(x, v, dist):
    for i in graph[x]:
        if dist[i[0]] == -1:
            dist[i[0]] = v + i[1]
            dfs(i[0], v + i[1], dist)


def search(s):
    dist = [-1] * (N + 1)
    dist[s] = 0
    dfs(s, 0, dist)
    return dist


root_dist = search(1)
far_dist = search(root_dist.index(max(root_dist)))
print(max(far_dist))
