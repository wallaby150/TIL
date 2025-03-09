import sys
input = sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
score = []

for i in range(N):
    a, b = map(int, input().split())
    if b <= M:
        score.append(140)
    elif a <= M:
        score.append(100)

score = sorted(score, reverse=True)
print(sum(score[:K]))
