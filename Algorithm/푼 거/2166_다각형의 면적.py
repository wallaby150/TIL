import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
dots.append(dots[0])
ans = 0

for i in range(N):
    a = dots[i][0] * dots[i+1][1]
    b = dots[i+1][0] * dots[i][1]
    ans += dots[i][0] * dots[i+1][1] - dots[i+1][0] * dots[i][1]

print(round(abs(ans) / 2, 1))
