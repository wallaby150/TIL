import sys
input = sys.stdin.readline

N = int(input())
a = b = c = 0
for _ in range(N):
    _, _, d = input().split()
    c = a + int(d)
    c = max(b, c)
    a, b = b, c
print(c)