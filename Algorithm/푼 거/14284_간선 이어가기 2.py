import sys, heapq as hq
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [10 ** 8] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

q = [(0, s)]
dist[s] = 0

while q:
    v, now = hq.heappop(q)

    for togo, tv in graph[now]:
        if dist[togo] > v + tv:
            dist[togo] = v + tv
            hq.heappush(q, (dist[togo], togo))

print(dist[t])
