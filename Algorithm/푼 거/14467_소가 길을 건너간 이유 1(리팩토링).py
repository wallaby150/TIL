import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cow = [-1] * 11
ans = 0

for _ in range(N):
    num, now = map(int, input().split())
    if cow[num] == -1:
        cow[num] = now
    else:
        if cow[num] != now:
            ans += 1
            cow[num] = now

print(ans)
