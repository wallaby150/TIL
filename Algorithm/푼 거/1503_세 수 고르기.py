import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
if M:
    S = set(map(int, input().split()))
else:
    S = set()
answer = float('inf')

for i in range(1, 1002):
    if i in S:
        continue
    for j in range(i, 1002):
        if j in S:
            continue
        for k in range(j, 1002):
            if k in S:
                continue
            now = abs(N - i * j * k)
            answer = min(answer, now)
            if answer == 0:
                break
            if now > N + 1:
                break
        if answer == 0:
            break
    if answer == 0:
        break

print(answer)