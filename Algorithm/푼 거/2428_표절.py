N = int(input())
nums = sorted(list(map(int, input().split())))
cnt = j = 0

for i in range(N-1):
    j = max(i+1, j)
    while j < N and nums[i] >= nums[j] * 0.9:
        j += 1
    cnt += j - i - 1

print(cnt)
