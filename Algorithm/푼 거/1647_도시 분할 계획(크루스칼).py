import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())
parents = [i for i in range(V+1)]
ans = 0

connects = [list(map(int, input().split())) for _ in range(E)]
connects.sort(key=lambda x: x[2])


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


last = 0
for connect in connects:
    a, b, c = connect
    if find(a) != find(b):
        union(a, b)
        ans += c
        last = c


print(ans - last)
