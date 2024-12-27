import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    ans = 0
    
    for i in range(1, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1

    print(nums[0], ans)
