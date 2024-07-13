import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    checked = [False] * (N * M)
    graph = [[0] * (N * M) for _ in range(N * M)]

    for i in range(N):
        nums = list(map(int, input().split()))
        for j in range(M-1):
            num = nums[j]
            graph[i * M + j][i * M + j+1] = num
            graph[i * M + j+1][i * M + j] = num

    for k in range(N-1):
        nums = list(map(int, input().split()))
        for l in range(M):
            num = nums[l]
            graph[k * M + l][(k+1) * M + l] = num
            graph[(k+1) * M + l][k * M + l] = num

    q = []
    heapq.heappush(q, (0, 0))
    ans = 0

    while q:
        cost, togo = heapq.heappop(q)
        if not checked[togo]:
            checked[togo] = True
            ans += cost

            for i in range(N * M):
                if graph[togo][i] != 0 and not checked[i]:
                    heapq.heappush(q, (graph[togo][i], i))
    print(ans)
