import sys
input = lambda : sys.stdin.readline().rstrip()

M = int(input())
answer = 0
l, r = 1, M * 5

while l <= r:
    mid = (l+r) // 2

    cnt = 0
    tmp = mid
    while tmp >= 5:
        cnt += tmp // 5
        tmp //= 5

    if cnt < M:
        l = mid + 1
    elif cnt >= M:
        if cnt == M:
            answer = mid
        r = mid - 1

if answer == 0:
    print(-1)
else:
    print(answer)