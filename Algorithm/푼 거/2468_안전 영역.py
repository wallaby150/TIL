import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
high, low = max(max(x) for x in nums), min(min(n) for n in nums)


def drown(level):
    grid = [[False] * N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if nums[y][x] < level:
                grid[y][x] = True

    return grid


def search(grid):
    visited = [[False] * N for _ in range(N)]

    place = 0
    for y in range(N):
        for x in range(N):
            # 잠겨 고, 안 가봤으면
            if not grid[y][x] and not visited[y][x]:
                place += 1

                # DFS 시작
                stack = [(y, x)]
                visited[y][x] = True
                while stack:
                    ny, nx = stack.pop()
                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ty, tx = ny + dy, nx + dx
                        if 0 <= ty < N and 0 <= tx < N and not grid[ty][tx] and not visited[ty][tx]:
                            visited[ty][tx] = True
                            stack.append((ty, tx))
    return place


ans = 0
for i in range(low, high+1):
    now = drown(i)
    cnt = search(now)
    ans = max(ans, cnt)

print(ans)
