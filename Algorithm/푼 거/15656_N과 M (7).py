N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def solve():
    if len(tmp) == M:
        print(*tmp)
        return

    for i in range(len(nums)):
        tmp.append(nums[i])
        solve()
        tmp.pop()

solve()
