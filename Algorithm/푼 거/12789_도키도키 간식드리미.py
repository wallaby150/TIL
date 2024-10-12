import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
stack = []
target = 1

while nums or stack:
    if nums and target == nums[0]:
        nums.pop(0)
        target += 1
    elif stack and target == stack[-1]:
        stack.pop()
        target += 1
    else:
        if nums:
            stack.append(nums.pop(0))
        else:
            print("Sad")
            break
else:
    print("Nice")