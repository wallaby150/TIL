import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = [0]
for _ in range(N):
    nums.append(nums[-1] + int(input()))

l, r = 0, 1
ans = 0

while l < r and r <= N:
    A = nums[r] - nums[l]
    B = nums[l] + nums[-1] - nums[r]

    ans = max(ans, min(A, B))

    if A == B:
        break
    elif A > B:
        l += 1
    else:
        r += 1

print(ans)
