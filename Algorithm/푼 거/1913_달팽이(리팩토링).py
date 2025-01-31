N = int(input())
target = int(input())

nums = [[0] * N for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 → 우 → 상 → 좌
cnt = N ** 2

y, x = 0, 0
way = 0
target_y, target_x = 0, 0

while cnt > 0:
    nums[y][x] = cnt
    if cnt == target:
        target_y, target_x = y + 1, x + 1

    cnt -= 1
    dy, dx = directions[way]
    ny, nx = y + dy, x + dx

    if not (0 <= ny < N and 0 <= nx < N and nums[ny][nx] == 0):
        way = (way + 1) % 4  # 방향 변경
        dy, dx = directions[way]
        ny, nx = y + dy, x + dx

    y, x = ny, nx  # 위치 갱신

for line in nums:
    print(" ".join(map(str, line)))
print(target_y, target_x)
