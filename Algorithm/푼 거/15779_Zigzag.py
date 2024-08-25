N = int(input())
nums = list(map(int, input().split()))
cnt = ans = 2

for i in range(N - 2):
    if nums[i] <= nums[i + 1] <= nums[i + 2]:
        cnt = 2
    elif nums[i] >= nums[i + 1] >= nums[i + 2]:
        cnt = 2
    else:
        cnt += 1

    ans = max(ans, cnt)
print(ans)
