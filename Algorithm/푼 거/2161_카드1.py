from collections import deque

N = int(input())
nums = deque(range(1, N+1))

while len(nums) > 1:
    print(nums.popleft(), end=' ')
    nums.append(nums.popleft())

print(nums[0])
