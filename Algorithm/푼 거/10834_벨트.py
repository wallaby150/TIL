import sys
input = lambda: sys.stdin.readline().rstrip()

m = int(input())
ans = 0
rotate = 0

for i in range(m):
    a, b, r = map(int, input().split())
    if i == 0:
        ans = a * b
    else:
        ans = int(ans / a * b)
    if r == 1:
        rotate = 1 - rotate

print(rotate, ans)
