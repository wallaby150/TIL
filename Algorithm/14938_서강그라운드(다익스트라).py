import sys, heapq
input = lambda: sys.stdin.readline().rstrip()
INF = sys.maxsize

# 지역수 N, 수색범위 M, 길의 개수 R
N, M, R = map(int, input().split())
# 각 구역의 아이템 수
T = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]


# 길 정보 받음
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

result = 0

for i in range(1, N + 1):
    q = []
    heapq.heappush(q, [0, i])
    distance = [15001] * (N + 1)
    distance[i] = 0

    # 다익스트라 시작
    while q:
        d, node = heapq.heappop(q)
        if d > distance[node]:
            continue

        for togo, v in graph[node]:
            if d + v < distance[togo]:
                distance[togo] = d + v
                heapq.heappush(q, [d + v, togo])

    tmp = 0
    for j in range(N):
        if distance[j+1] <= M:
            tmp += T[j]

    result = max(result, tmp)

print(result)