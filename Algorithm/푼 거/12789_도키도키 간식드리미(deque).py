import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = deque(map(int, input().split()))
stack = []
target = 1

while nums or stack:
    if nums and target == nums[0]:
        nums.popleft()
        target += 1
    elif stack and target == stack[-1]:
        stack.pop()
        target += 1
    else:
        if nums:
            stack.append(nums.popleft())
        else:
            print("Sad")
            break
else:
    print("Nice")