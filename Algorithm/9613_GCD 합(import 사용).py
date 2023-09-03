import sys
from itertools import combinations
from math import gcd
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    ans = 0

    n, *nums = map(int, input().split())
    tmp = list(combinations(nums, 2))
    for comb in tmp:
        ans += gcd(*comb)

    print(ans)