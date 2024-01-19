N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))
tmp = []


def solve(depth, idx):
    if depth == M:
        print(*tmp)
        return

    for i in range(idx, len(nums)):
        tmp.append(nums[i])
        solve(depth + 1, i)
        tmp.pop()

solve(0, 0)