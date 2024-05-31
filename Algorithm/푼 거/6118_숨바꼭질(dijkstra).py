import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [set() for _ in range(N+1)]
dist = [20001] * (N + 1)
dist[0] = dist[1] = 0

for _ in range(M):
    S, E = map(int, input().split())
    grid[S].add(E)
    grid[E].add(S)

h = []
heapq.heappush(h, (0, 1))

while h:
    d, n = heapq.heappop(h)
    for j in grid[n]:
        if dist[j] > d + 1:
            dist[j] = d + 1
            heapq.heappush(h, (d+1, j))

far = max(dist)
print(dist.index(far), far, dist.count(far))