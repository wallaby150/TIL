def solve(nums):
    n = len(nums)
    i = 0
    while i < n - 1 and nums[i] < nums[i + 1]:
        i += 1

    while i < n - 1 and nums[i] > nums[i + 1]:
        i += 1

    return i == n - 1


N = int(input())
nums = list(map(int, input().split()))

print("YES" if solve(nums) else "NO")
