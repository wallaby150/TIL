import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cloud = ((N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1))  # 초기 구름 위치
direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
             5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}  # 8방향 정의

def make_cloud(banned_spot):
    global cloud
    cloud = set()
    for y in range(N):
        for x in range(N):
            if (y, x) not in banned_spot and grid[y][x] >= 2:
                grid[y][x] -= 2
                cloud.add((y, x))  # 새로운 구름 생성

def water_bug(rained_spots):
    for ry, rx in rained_spots:
        for d in [2, 4, 6, 8]:  # 대각선 방향 체크
            dy, dx = direction[d]
            ty, tx = ry + dy, rx + dx
            if 0 <= ty < N and 0 <= tx < N and grid[ty][tx]:
                grid[ry][rx] += 1  # 물복사버그 마법 적용
    make_cloud(rained_spots)

def move_and_rain(before, d, s):
    dy, dx = direction[d]
    now = set()
    for ny, nx in before:
        ty, tx = (ny + dy * s) % N, (nx + dx * s) % N  # 구름 이동
        now.add((ty, tx))
        grid[ty][tx] += 1  # 비 내리기
    water_bug(now)

for _ in range(M):
    di, si = map(int, input().split())
    move_and_rain(cloud, di, si)

print(sum(sum(grid[i]) for i in range(N)))  # 총 물의 양 계산