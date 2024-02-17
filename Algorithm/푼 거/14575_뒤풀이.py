import sys
input = lambda : sys.stdin.readline().rstrip()

N, T = map(int, input().split())
nums = []
low, high = 0, 0

for _ in range(N):
    a, b = map(int, input().split())
    low += a
    high += b
    nums.append([a, b])

if not low <= T <= high:
    print(-1)
else:
    l, r = max(nums, key=lambda x: x[0])[0], max(nums, key=lambda x: x[1])[1]

    def solve(num):
        tmp = 0
        for i in nums:
            tmp += min(num, i[1])
        return tmp

    while l <= r:
        m = (l + r) // 2
        drink = solve(m)

        if drink == T:
            break
        elif drink > T:
            r = m - 1
        else:
            l = m + 1

    print(m)