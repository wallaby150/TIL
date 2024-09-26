import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = []

for i in range(N):
    x, y, v = map(int, input().split())
    cal = (x ** 2 + y ** 2) ** 0.5 / v
    ans.append((cal, i + 1))

ans.sort()
for j in ans:
    print(j[1])
