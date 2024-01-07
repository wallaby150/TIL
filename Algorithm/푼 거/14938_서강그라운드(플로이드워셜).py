import sys
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

# 지역수 N, 수색범위 M, 길의 개수 R
N, M, R = map(int, input().split())
# 각 구역의 아이템 수
T = list(map(int, input().split()))
dist = [[INF] * (N) for _ in range(N)]

# 초기화
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

# 길 정보 받음
for _ in range(R):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

# 플로이드 워셜 시작
for k in range(N):
    for l in range(N):
        for m in range(N):
            dist[l][m] = min(dist[l][m], dist[l][k] + dist[k][m])

answer = 0

# 각 지역별로 얻을 수 있는 값 계산
for line in dist:
    tmp = 0
    for idx in range(N):
        if line[idx] <= M:
            tmp += T[idx]
    answer = max(answer, tmp)

print(answer)