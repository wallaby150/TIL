N = int(input())
nums = [[0] * N for _ in range(N)]
target = int(input())

cnt = N ** 2
stack = [(0, 0)]
way = 0
direction_dict = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
target_y, target_x = 0, 0

while stack:
    ny, nx = stack.pop()
    nums[ny][nx] = cnt

    if cnt == target:
        target_y, target_x = ny + 1, nx + 1

    cnt -= 1

    if cnt == 0:
        break

    dy, dx = direction_dict[way]
    ty, tx = ny + dy, nx + dx
    if (ty < 0 or ty >= N or tx < 0 or tx >= N) or nums[ty][tx] != 0:
        way = (way + 1) % 4
        dy, dx = direction_dict[way]
        ty, tx = ny + dy, nx + dx

    stack.append((ty, tx))

for line in nums:
    print(" ".join(map(str, line)))
print(target_y, target_x)
