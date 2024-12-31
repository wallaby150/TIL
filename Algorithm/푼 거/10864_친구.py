import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
count = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1

for i in range(1, N + 1):
    print(count[i])