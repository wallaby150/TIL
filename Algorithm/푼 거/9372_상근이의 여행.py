import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    print(N-1)
