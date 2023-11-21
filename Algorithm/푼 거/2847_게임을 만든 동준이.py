import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
scores = list(int(input()) for _ in range(N))
answer = 0

for idx in range(N-2, -1, -1):
    now, next = scores[idx], scores[idx + 1]
    if now >= next:
        diff = now - next + 1
        answer += diff
        scores[idx] -= diff

print(answer)