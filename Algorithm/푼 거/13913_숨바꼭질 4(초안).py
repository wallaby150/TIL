import sys
from collections import deque
sys.setrecursionlimit(10 ** 8)
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    print(*range(N, K-1, -1))
else:
    # 숫자 x까지 오는데 필요한 이동 수, 이전 숫자
    dp = [[0, 0] for _ in range(K * 2 + 1)]
    # dp[N][0] = -1

    q = deque([(N, 0)])
    while q:
        now, move = q.popleft()

        if now == K:
            break

        for tx in [now-1, now+1, now*2]:
            if 0 <= tx < K * 2 and dp[tx][0] == 0:
                dp[tx][0] = move + 1
                dp[tx][1] = now
                q.append((tx, move + 1))

    def dfs(num, arr):
        if num == N:
            return [num] + arr
        return dfs(dp[num][1], [num] + arr)

    print(dp[K][0])
    print(*dfs(K, []))