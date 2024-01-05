import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

N = int(input())
M = int(input())
dist = [[INF] * (N) for _ in range(N)]

# 초기화
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

# 버스값 받음
for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

# 플로이드 워셜 시작
for k in range(N):
    for l in range(N):
        for m in range(N):
            dist[l][m] = min(dist[l][m], dist[l][k] + dist[k][m])

for line in dist:
    for num in line:
        if num == INF:
            print(0, end=' ')
        else:
            print(num, end=' ')
    print()