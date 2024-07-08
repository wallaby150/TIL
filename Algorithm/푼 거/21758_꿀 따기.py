N = int(input())
nums = list(map(int, input().split()))
haps = [nums[0]]
for i in range(1, N):
    haps.append(haps[i-1] + nums[i])

# 벌꿀통 가운데
ans = haps[-2] - nums[0] + max(nums[1:-1])

# 벌꿀통 제일 왼쪽
tmp1 = haps[-2]
# 벌꿀통 제일 오른쪽
tmp2 = haps[-1] * 2 - nums[0]
for j in range(1, N-1):
    ans = max(ans, tmp1 + haps[j-1] - nums[j])
    ans = max(ans, tmp2 - haps[j] - nums[j])

print(ans)
