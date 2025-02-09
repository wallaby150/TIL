nums = [int(input()) for _ in range(5)]
X = nums[4] * nums[0]
Y = nums[1] + nums[3] * max(0, nums[4] - nums[2])
print(min(X, Y))
