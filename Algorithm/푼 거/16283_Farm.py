a, b, n, w = map(int, input().split())
cnt = 0

for i in range(1, n):
    A, B = i, n - i
    if A * a + B * b == w:
        s, g = A, B
        cnt += 1

if cnt == 1:
    print(s, g)
else:
    print(-1)
