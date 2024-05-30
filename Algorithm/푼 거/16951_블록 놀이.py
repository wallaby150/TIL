import sys
input = lambda: sys.stdin.readline().rstrip()


def check(i):
    cnt = 0
    for j in range(N):
        if j < i:
            if nums[j] != (nums[i] - (i - j) * K):
                cnt += 1
        elif j > i:
            if nums[j] != (nums[i] + (j - i) * K):
                cnt += 1
    return cnt


N, K = map(int, input().split())
nums = list(map(int, input().split()))
ans = 1001

for i in range(N):
    if nums[i] > i * K:
        ans = min(ans, check(i))

print(ans)
