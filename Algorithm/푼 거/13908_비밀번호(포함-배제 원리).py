import sys
from math import factorial
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
if M > 0:
    input()
ans = 10 ** N


def comb(a, b):
    return factorial(a) // (factorial(b) * factorial(a - b))


for i in range(1, M + 1):
    ans += (((-1) ** i) * (comb(M, i)) * ((10 - i) ** N))
print(ans)
