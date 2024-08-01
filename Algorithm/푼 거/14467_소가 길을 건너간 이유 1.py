import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
cow = {}
ans = 0

for _ in range(N):
    num, now = map(int, input().split())
    if num not in cow:
        cow[num] = now
    else:
        if cow[num] != now:
            ans += 1
            cow[num] = now

print(ans)
