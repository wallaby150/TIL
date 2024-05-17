
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
ans = 1

for i in range(1, N + 1):
    ans *= i

print(str(int(str(ans)[::-1]))[0])
