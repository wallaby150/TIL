nums = sorted(map(int, input().split()))
ans = nums[0] + nums[1] + min(nums[2], nums[0] + nums[1] - 1)
print(ans)
