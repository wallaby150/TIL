import sys
input = lambda : sys.stdin.readline().rstrip()

N, restrict_N, A, B = map(int, input().split())
restricts = list(list(map(int, input().split())) for _ in range(restrict_N))

minimum_n = [1000001] * (N + 1)

for restrict in restricts:
    minimum_n[restrict[0]:restrict[1]+1] = [-1] * (restrict[1] - restrict[0]+1)
minimum_n[0] = 0
possibles = {0}

while possibles:
    now = possibles.pop()
    if now + A <= N and minimum_n[now + A] > minimum_n[now] + 1:
        minimum_n[now + A] = minimum_n[now] + 1
        possibles.add(now + A)
    if now + B <= N and minimum_n[now + B] > minimum_n[now] + 1:
        minimum_n[now + B] = minimum_n[now] + 1
        possibles.add(now + B)


if minimum_n[N] == 1000001:
    print(-1)
else:
    print(minimum_n[N])