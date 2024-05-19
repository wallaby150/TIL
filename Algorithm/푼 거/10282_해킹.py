import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
INF = float("inf")
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)

    for _ in range(D):
        e, s, w = map(int, input().split())
        graph[s].append((e, w))

    q = []
    heapq.heappush(q, (0, C))
    dist[C] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for i in graph[now]:
            if d + i[1] < dist[i[0]]:
                dist[i[0]] = d + i[1]
                heapq.heappush(q, (d + i[1], i[0]))

    cnt, far = 0, 0
    for j in dist:
        if j != INF:
            cnt += 1
            far = max(far, j)

    print(cnt, far)
