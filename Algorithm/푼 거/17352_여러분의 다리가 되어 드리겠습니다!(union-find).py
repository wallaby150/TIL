import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

if N == 2:
    print(1, 2)
else:
    def find(c):
        if c == P[c]:
            return c
        else:
            P[c] = find(P[c])
            return P[c]


    def union(x, y):
        px, py = find(x), find(y)
        if px > py:
            P[px] = py
        else:
            P[py] = px
        return


    P = list(range(N+1))
    for _ in range(N-2):
        a, b = map(int, input().split())
        union(a, b)

    left = find(1)
    for i in range(2, N+1):
        if left != find(i):
            print(1, i)
            break
