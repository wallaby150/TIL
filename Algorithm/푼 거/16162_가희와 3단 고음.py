N, A, D = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
target = A

for i in range(N):
    if nums[i] == target:
        ans += 1
        target += D

print(ans)