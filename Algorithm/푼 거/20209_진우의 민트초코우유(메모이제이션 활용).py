import sys
input = lambda: sys.stdin.readline().rstrip()

# 마을 크기 N, 초기 체력 M, 증가 체력 H
N, M, H = map(int, input().split())
milks = []
ans = 0
home = (-1, -1)

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(N):
        if line[x] == 2:
            milks.append((y, x))
        elif line[x] == 1:
            home = (y, x)

# 메모이제이션을 위한 딕셔너리
memo = {}

def cal_dist(y1, x1, y2, x2):
    return abs(y1-y2) + abs(x1-x2)

def dfs(ny, nx, hp, drink, visited):
    global ans

    if (ny, nx, hp, visited) in memo:
        return memo[(ny, nx, hp, visited)]

    if cal_dist(ny, nx, home[0], home[1]) <= hp:
        ans = max(ans, drink)

    max_drinks = drink

    for i, (my, mx) in enumerate(milks):
        if not (visited & (1 << i)):
            dist = cal_dist(ny, nx, my, mx)
            if dist <= hp:
                max_drinks = max(max_drinks, dfs(my, mx, hp - dist + H, drink + 1, visited | (1 << i)))

    memo[(ny, nx, hp, visited)] = max_drinks
    return max_drinks

dfs(home[0], home[1], M, 0, 0)
print(ans)
