import sys, math
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(math.lcm(a, b))
