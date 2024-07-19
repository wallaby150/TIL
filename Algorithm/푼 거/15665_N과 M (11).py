N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))


def solve(now):
    if len(now) == M:
        print(*now)
        return

    for i in range(len(nums)):
        now.append(nums[i])
        solve(now)
        now.pop()
    return

solve([])
