import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

# 집 갯수 N, 도로 갯수 M, 가능 거리 X, 내집 Y
N, M, X, Y = map(int, input().split())
dist = [1e8] * N

graph = {i : [] for i in range(N)}
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for j in graph[now]:
            if d + j[1] < dist[j[0]]:
                dist[j[0]] = d+j[1]
                heapq.heappush(q, (d+j[1], j[0]))


dijkstra(Y)

if max(dist) * 2 <= X:
    short = sorted(dist)
    day = 1
    time = 0

    for k in short:
        if time + k * 2 <= X:
            time += k * 2
        else:
            day += 1
            time = 2 * k

    print(day)
else:
    print(-1)