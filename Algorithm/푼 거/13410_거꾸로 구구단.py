import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
answer = set()
for i in range(1, K+1):
    answer.add(int(str(N * i)[::-1]))

print(max(answer))