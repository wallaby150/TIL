import sys
sys.setrecursionlimit(10 ** 6)
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
cnt = 0


def find(z):
    if parent[z] != z:
        parent[z] = find(parent[z])
    return parent[z]


def union(a, b):
    c = find(a)
    d = find(b)

    if rank[c] > rank[d]:
        parent[d] = c
    elif rank[c] < rank[d]:
        parent[c] = d
    else:
        parent[d] = c
        rank[d] += 1


for _ in range(M):
    x, y = map(int, input().split())

    if find(x) == find(y):
        cnt += 1
    else:
        union(x, y)


tmp = set()
for j in range(1, N+1):
    tmp.add(find(j))

print(len(tmp) - 1 + cnt)
