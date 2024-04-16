import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(z):
    if parent[z] != z:
        parent[z] = find(parent[z])
    return parent[z]


def union(a, b):
    c = find(a)
    d = find(b)

    if c < d:
        parent[d] = c
    else:
        parent[c] = d


for _ in range(M):
    com, x, y = map(int, input().split())
    if com == 0:
        union(x, y)

    elif com == 1:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
