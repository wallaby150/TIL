N, M = map(int, input().split())
nums = list(range(1, N+1))
tmp = []


def solve(idx):
    if len(tmp) == M:
        print(*tmp)
        return

    if len(tmp) + N - idx < M:
        return

    for i in range(idx, N):
        tmp.append(nums[i])
        solve(i + 1)
        tmp.pop()

solve(0)