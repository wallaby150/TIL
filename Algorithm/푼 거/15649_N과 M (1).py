import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(range(1, N+1))

for a in permutations(nums, M):
    print(*a)