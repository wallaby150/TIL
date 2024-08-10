import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
ans = deque([])
nums.reverse()

for i in range(N):
    if nums[i] == 1:
        ans.appendleft(i + 1)
    elif nums[i] == 2:
        ans.insert(1, i + 1)
    else:
        ans.append(i + 1)

print(*ans)
