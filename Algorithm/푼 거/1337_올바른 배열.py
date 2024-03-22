N = int(input())
nums = sorted([int(input()) for _ in range(N)])
check = set(nums)
l, r = 0, 0
ans = 5

for i in range(N):
    cnt = 0
    for j in range(nums[i] + 1, nums[i] + 5):
        if j not in check:
            cnt += 1
    ans = min(cnt, ans)

print(ans)