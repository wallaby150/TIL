N = int(input())
nums = list(map(int, input().split()))
ans = sum(nums, max(nums))/2
print(ans)
