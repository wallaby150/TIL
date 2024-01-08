import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

# 도시의 수 N
N = int(input())
# 버스의 개수
M = int(input())
dist = [[INF] * (N) for _ in range(N)]
way = [[[0]] * N for _ in range(N)]

# 초기화
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

# 길 정보 받음
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
    way[a-1][b-1] = [a, b]



# 플로이드 워셜 시작
for k in range(N):
    for l in range(N):
        for m in range(N):
            if dist[l][m] > dist[l][k] + dist[k][m]:
                dist[l][m] = dist[l][k] + dist[k][m]
                way[l][m] = [*way[l][k], *way[k][m][1:]]

for line in dist:
    for v in line:
        if v == INF:
            print(0, end=' ')
        else:
            print(v, end=' ')
    print()

for o in range(N):
    for p in range(N):
        if way[o][p] == [0]:
            print(0)
        else:
            print(len(way[o][p]), *way[o][p])