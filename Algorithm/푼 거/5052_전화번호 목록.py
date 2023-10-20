import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    n = int(input())

    nums = []
    for _ in range(n):
        nums.append(input())

    nums.sort()

    answer = True
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            answer = False
            break

    if answer:
        print("YES")
    else:
        print("NO")