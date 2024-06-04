import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    ans = 0

    for _ in range(N):
        tx, ty, r = map(int, input().split())
        cnt = 0
        for x, y in [(x1, y1), (x2, y2)]:
            if (x-tx) ** 2 + (y-ty) ** 2 <= r ** 2:
                cnt += 1

        if cnt == 1:
            ans += 1

    print(ans)

