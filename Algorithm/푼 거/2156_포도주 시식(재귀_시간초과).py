import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(int(input()) for _ in range(N))
dp = [[0, 0, 0] for _ in range(N+1)]


def solve(now, idx, row):
    if idx == N:
        return

    # 이미 2잔 마셨으면 3잔째는 패스
    if row < 2:
        if dp[idx+1][row+1] < now + nums[idx]:
            dp[idx+1][row+1] = now + nums[idx]
            solve(now + nums[idx], idx+1, row+1)

    if dp[idx+1][0] < now:
        dp[idx+1][0] = now
        solve(now, idx+1, 0)


solve(0, 0, 0)
print(max(dp[-1]))