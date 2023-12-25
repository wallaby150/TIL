import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = set()

for com in permutations(nums, M):
    answer.add(com)

for a in sorted(list(answer)):
    print(*a)