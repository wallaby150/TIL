import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
dp = [1001] * N
dp[0] = 0
q = deque([0])

while q:
    idx = q.popleft()
    num = nums[idx]
    for i in range(1, min(num+1, N-1)):
        togo = min(idx + i, N-1)
        if dp[togo] > dp[idx] + 1:
            dp[togo] = dp[idx] + 1
            q.append(togo)


if dp[N-1] == 1001:
    print(-1)
else:
    print(dp[N-1])