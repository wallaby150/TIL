N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []


def solve(idx):
    if len(tmp) == M:
        print(*tmp)
        return

    last = 0
    for i in range(idx, N):
        if last != nums[i]:
            tmp.append(nums[i])
            last = nums[i]
            solve(i)
            tmp.pop()

solve(0)