import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
C_list = [list(map(int, input().split())) for _ in range(N)]

X = sorted(C_list, key = lambda x : x[0])[N//2][0]
Y = sorted(C_list, key = lambda x : x[1])[N//2][1]
ans = 0

for c in C_list:
    ans += abs(X - c[0]) + abs(Y - c[1])

print(ans)