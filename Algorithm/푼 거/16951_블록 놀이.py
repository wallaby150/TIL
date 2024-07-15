import sys
input = lambda: sys.stdin.readline().rstrip()


def check(x):
    cnt = 0
    for j in range(N):
        if j < x:
            if nums[j] != nums[x] - (x - j) * K:
                cnt += 1
        elif j > x:
            if nums[j] != nums[x] + (j - x) * K:
                cnt += 1
    return cnt


N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 1001

for i in range(N):
    if nums[i] > i * K:
        ans = min(ans, check(i))

print(ans)
