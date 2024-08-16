import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
visited = [False] * (V + 1)
ans = 0

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = [(0, 1)]
# 방문한 노드의 갯수
cnt = 0
while q and cnt < V:
    price, now = heapq.heappop(q)
    # 아직 안 가봤으면
    if not visited[now]:
        visited[now] = True
        ans += price
        cnt += 1

        for togo, tv in graph[now]:
            if not visited[togo]:
                heapq.heappush(q, (tv, togo))

print(ans)