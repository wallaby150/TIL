N = int(input())
nums = list(map(int, input().split()))

total_sum = sum(nums)
ans = 0

for i in range(N - 1):
    total_sum -= nums[i]
    ans += nums[i] * total_sum

print(ans)
