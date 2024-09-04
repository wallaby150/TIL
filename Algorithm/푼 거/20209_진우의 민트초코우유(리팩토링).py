import sys
input = lambda: sys.stdin.readline().rstrip()

# 마을 크기 N, 초기 체력 M, 증가 체력 H
N, M, H = map(int, input().split())
milks = []
ans = 0

for y in range(N):
    row = list(map(int, input().split()))
    for x in range(N):
        if row[x] == 2:
            milks.append((y, x))
        elif row[x] == 1:
            # 집의 좌표
            hy, hx = y, x

milks = [(hy, hx)] + milks
l = len(milks)
visited = [False] * l


def cal_dist(y1, x1, y2, x2):
    return abs(y1-y2) + abs(x1-x2)


graph = [[-1] * l for _ in range(l)]
for y in range(l):
    for x in range(l):
        if y == x:
            graph[y][x] = 0
        else:
            graph[y][x] = cal_dist(*milks[y], *milks[x])


def solve(idx, hp, drink):
    global ans

    if ans == l - 1:
        return

    # 마신 게 있고, 돌아갈 체력도 있다면
    if drink and graph[idx][0] <= hp:
        ans = max(ans, drink)

    for i in range(1, l):
        # 안 가봤고
        if not visited[i]:
            dist = graph[idx][i]
            if dist <= hp:
                visited[i] = True
                solve(i, hp - dist + H, drink + 1)
                visited[i] = False


solve(0, M, 0)
print(ans)
