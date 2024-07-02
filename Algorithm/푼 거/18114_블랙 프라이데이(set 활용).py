import sys
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, C = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    tmp = set([0] + nums)

    if C in tmp:
        return 1

    l, r = 0, N - 1
    while l < r:
        s, e = nums[l], nums[r]
        a = C - s - e
        if a != s and a != e and a in tmp:
            return 1
        if a < 0:
            r -= 1
        else:
            l += 1

    return 0


print(solve())
