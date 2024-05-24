import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
S = int(input())

INF = float('inf')
dist = [INF] * (V+1)
dist[S] = 0

graph = [{} for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

q = [(0, S)]
while q:
    nd, s = heapq.heappop(q)
    if dist[s] < nd:
        continue

    for e, d in graph[s].items():
        if dist[e] > nd + d:
            dist[e] = nd + d
            heapq.heappush(q, (nd+d, e))

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
