import sys, heapq
input = lambda: sys.stdin.readline().rstrip()


def dijkstra():
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    visited[0][0] = grid[0][0]
    q = [(grid[0][0], 0, 0)]

    while q:
        v, y, x = heapq.heappop(q)

        if y == x == N - 1:
            break

        if visited[y][x] < v:
            continue

        for dy, dx in direction:
            ty, tx = y + dy, x + dx
            if 0 <= ty < N and 0 <= tx < N:
                tv = v + grid[ty][tx]
                if visited[ty][tx] > tv:
                    visited[ty][tx] = tv
                    heapq.heappush(q, (tv, ty, tx))

    print(f'Problem {test_case}: {visited[-1][-1]}')


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
test_case = 0
while True:
    test_case += 1
    N = int(input())
    if not N:
        break

    dijkstra()
