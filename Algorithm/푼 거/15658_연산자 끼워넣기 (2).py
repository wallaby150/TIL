import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
# +, -, X, /
cal = list(map(int, input().split()))
high, low = -1000000001, 1000000001


def solve(index, num):
    global high, low

    if index == N:
        high = max(high, num)
        low = min(low, num)
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            if i == 0:
                solve(index + 1, num + nums[index])
            elif i == 1:
                solve(index + 1, num - nums[index])
            elif i == 2:
                solve(index + 1, num * nums[index])
            else:
                solve(index + 1, int(num / nums[index]))
            cal[i] += 1


solve(1, nums[0])

print(high)
print(low)