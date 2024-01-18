N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []


def solve(idx):
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(idx, N):
        tmp.append(nums[i])
        solve(i)
        tmp.pop()

solve(0)