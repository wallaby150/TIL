import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
ans = []

def solve(idx, depth):
    if depth == M:
        print(*ans)
        return

    for i in range(idx, N - (M - depth) + 1):
        ans.append(nums[i])
        solve(i + 1, depth + 1)
        ans.pop()

solve(0, 0)
