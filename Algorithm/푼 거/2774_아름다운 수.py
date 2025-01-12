import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    x = set(input())
    print(len(x))