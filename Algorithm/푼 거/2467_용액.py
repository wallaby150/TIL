import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
ans = [0, 0]
diff = 10 ** 10
l, r = 0, N - 1

while l < r:
    tmp = nums[l] + nums[r]

    if diff > abs(tmp):
        diff = abs(tmp)
        ans = [nums[l], nums[r]]

    if tmp == 0:
        break
    elif tmp > 0:
        r -= 1
    else:
        l += 1

print(*ans)