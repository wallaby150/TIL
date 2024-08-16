import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
walls = [True] * N

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a, b):
        walls[i] = False

print(sum(walls))
