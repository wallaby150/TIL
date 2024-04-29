import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [set(map(int, input().split())) for _ in range(N)]
ans = [0, 0]

for g in range(1, 6):
    tmp = 0

    for num in nums:
        if g in num:
            tmp += 1
        else:
            if ans[0] < tmp:
                ans = [tmp, g]
            tmp = 0
    else:
        if ans[0] < tmp:
            ans = [tmp, g]

print(*ans)