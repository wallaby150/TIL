import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    print(*range(N, K - 1, -1))
else:
    max_limit = max(N, K) * 2
    dp = [[0, -1] for _ in range(max_limit + 1)]

    q = deque([N])
    dp[N][0] = 0

    while q:
        now = q.popleft()

        if now == K:
            break

        for tx in [now - 1, now + 1, now * 2]:
            if 0 <= tx <= max_limit and dp[tx][0] == 0 and tx != N:
                dp[tx][0] = dp[now][0] + 1
                dp[tx][1] = now
                q.append(tx)

    # 경로 역추적
    path = []
    current = K
    while current != -1:
        path.append(current)
        current = dp[current][1]

    print(dp[K][0])
    print(*reversed(path))