import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

# 경유지
for i in range(N):
    # 시작지
    for j in range(N):
        # 도착지
        for k in range(N):
            if land[j][k] > land[j][i] + land[i][k]:
                land[j][k] = land[j][i] + land[i][k]

for _ in range(M):
    s, e, t = map(int, input().split())
    if land[s-1][e-1] <= t:
        print("Enjoy other party")
    else:
        print("Stay here")


