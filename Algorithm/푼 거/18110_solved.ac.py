import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
if N == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(N)]
    nums.sort()
    EPS = 1e-9

    c = round(N * 0.15 + EPS)
    print(round(sum(nums[c:-c] if c else nums) / (N - 2 * c) + EPS))