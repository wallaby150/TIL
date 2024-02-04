import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
D = {}

for _ in range(N):
    a, b = map(int, input().split())
    if b in D:
        D[b].append(a)
    else:
        D[b] = [a]

D = D.values()

ans = 0

for arr in D:
    arr.sort()
    if len(arr) <= 1:
        continue
    ans += abs(arr[0] - arr[1]) + abs(arr[-1] - arr[-2])
    for j in range(1, len(arr) - 1):
        ans += min(abs(arr[j] - arr[j - 1]), abs(arr[j] - arr[j + 1]))

print(ans)
