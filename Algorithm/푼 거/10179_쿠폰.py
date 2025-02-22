import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    p = float(input())
    print("$%.2f" % round(p * 0.8, 2))
