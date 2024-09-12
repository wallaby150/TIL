import sys
input = lambda: sys.stdin.readline().rstrip()


def find(z):
    if z != parents[z]:
        parents[z] = find(parents[z])
    return parents[z]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:  # 두 루트가 같지 않을 때만 합침
        if x > y:
            parents[x] = y
        else:
            parents[y] = x


# 트리인지 확인하는 dfs
def dfs(s):
    visited = [False] * (N+1)
    stack = [(0, s)]
    visited[s] = True

    while stack:
        parent, now = stack.pop()
        nexts = tree[now]
        for next in nexts:
            if next == parent:
                continue
            if visited[next]:
                return False
            visited[next] = True
            stack.append((now, next))

    return True


test_number = 0
while True:
    test_number += 1
    N, M = map(int, input().split())
    if N == M == 0:
        break

    parents = [e for e in range(N + 1)]
    tree = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, (input().split()))
        union(a, b)
        tree[a].append(b)
        tree[b].append(a)

    ans = set()
    for i in range(1, N + 1):
        num = find(i)  # 각 노드의 루트를 찾음
        if num not in ans:
            if dfs(num):
                ans.add(num)

    l = len(ans)
    if l == 0:
        print(f'Case {test_number}: No trees.')
    elif l == 1:
        print(f'Case {test_number}: There is one tree.')
    else:
        print(f'Case {test_number}: A forest of {l} trees.')
