N = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)
ans = 0

for i in range(N):
    if nums[i] + 1 + i > ans:
        ans = nums[i] + 1 + i

print(ans + 1)

