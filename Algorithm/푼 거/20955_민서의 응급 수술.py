import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
cnt = 0


def find(z):
    if parent[z] != z:
        return find(parent[z])
    return z


def union(a, b):
    global cnt

    c = find(a)
    d = find(b)

    if c < d:
        parent[d] = c
    elif c > d:
        parent[c] = d
    else:
        parent[d] = c
        cnt += 1


for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)


tmp = set()
for j in range(1, N+1):
    tmp.add(find(j))

print(len(tmp) - 1 + cnt)