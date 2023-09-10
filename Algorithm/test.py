import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
ground = [0] * 1000001
last = 0

for _ in range(N):
    i, g = map(int, input().split())
    ground[g] = i
    last = max(last, g)

ans = 0

for i in range(last - K + 1):
    a = ground[max(i-K, 0):i+K+1]
    ans = max(ans, sum(ground[max(i-K, 0):i+K+1]))

print(ans)