import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
high, low = max(max(l) for l in nums), min(min(l) for l in nums)


def drown():
    visited = [[False] * N for _ in range(N)]
    


for i in range(low, high):
    now = drown()