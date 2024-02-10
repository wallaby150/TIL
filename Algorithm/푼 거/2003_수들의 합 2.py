import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = list(map(int, input().split()))

tmp = nums[0]
l, right = 0, 1
ans = 0

while True:
    if tmp < M:
        if right < N:
            tmp += nums[right]
            right += 1
        else:
            break
    elif tmp == M:
        ans += 1
        tmp -= nums[l]
        l += 1
    else:
        tmp -= nums[l]
        l += 1

print(ans)