import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []

def solve(idx):
    if len(ans) == M:
        print(*ans)
        return

    if idx == N:
        return

    ans.append(nums[idx])
    solve(idx + 1)
    ans.pop()
    solve(idx + 1)

solve(0)