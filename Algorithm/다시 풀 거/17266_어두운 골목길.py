import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
settable_list = list(map(int, input().split()))

ans = 0

if M == 0:
    ans = max(settable_list[0], N - settable_list[0])
else:
    for i in range(M+1):
        if i == 0:
            height = settable_list[i]
        elif i == M:
            height = N - settable_list[i-1]
        else:
            temp = settable_list[i] - settable_list[i-1]
            # 홀수면
            if temp % 2:
                height = temp // 2 + 1
            else:
                height = temp // 2

        ans = max(height, ans)

print(ans)