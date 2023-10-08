import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
start, end = 0, 0
q = defaultdict(int)

while end < N:
    now = nums[end]

    if q[now] >= K:
        back = nums[start]
        q[back] -= 1
        start += 1

    else:
        q[now] += 1
        end += 1
        ans = max(ans, end - start)

print(ans)