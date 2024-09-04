import sys
input = lambda: sys.stdin.readline().rstrip()

# 마을 크기 N, 초기 체력 M, 증가 체력 H
N, M, H = map(int, input().split())
milks = []
visited = dict()
ans = 0

for y in range(N):
    line = list(map(int, input().split()))
    for x in range(N):
        if line[x] == 2:
            milks.append((y, x))
            visited[(y, x)] = False
        elif line[x] == 1:
            # 집의 좌표
            hy, hx = y, x


def cal_dist(y1, x1, y2, x2):
    return abs(y1-y2) + abs(x1-x2)


def dfs(ny, nx, hp, drink):
    global ans

    if ans == len(milks):
        return

    if drink and cal_dist(ny, nx, hy, hx) <= hp:
        ans = max(ans, drink)

    for milk in milks:
        if not visited[milk]:
            dist = cal_dist(ny, nx, *milk)
            # 아직 안 가봤고, 갈 수 있으면
            if dist <= hp:
                visited[milk] = True
                dfs(*milk, hp - dist + H, drink + 1)
                visited[milk] = False


dfs(hy, hx, M, 0)
print(ans)
