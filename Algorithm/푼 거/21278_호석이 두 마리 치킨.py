import sys
input = lambda : sys.stdin.readline().rstrip()

# 건물 갯수와 도로 갯수
N, M = map(int, input().split())
land = [[100] * (N) for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    land[s - 1][e - 1] = 1
    land[e - 1][s - 1] = 1

for num in range(N):
    land[num][num] = 0

# 경유지
for i in range(N):
    # 시작지
    for j in range(N):
        # 도착지
        for k in range(N):
            if land[j][k] > land[j][i] + land[i][k]:
                land[j][k] = land[j][i] + land[i][k]

ans = 20000
a, b = 10000, 10000

for x in range(N-1):
    for y in range(x+1, N):
        tmp = 0
        for t in range(N):
            tmp += min(land[x][t] * 2, land[y][t] * 2)
        if ans > tmp:
            ans = tmp
            a, b = x, y

print(a+1, b+1, ans)