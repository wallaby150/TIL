import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N)]
parent = list(map(int, input().split()))

for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)

x = int(input())

if x == root:
    print(0)
else:
    stack = []
    cnt = 0

    for c in tree[root]:
        if c != x:
            stack.append(c)

    if not stack:
        cnt += 1

    while stack:
        node = stack.pop()
        tmp = []
        for child in tree[node]:
            if child == x:
                continue
            else:
                tmp.append(child)

        if len(tmp) == 0:
            cnt += 1
        else:
            stack.extend(tmp)

    print(cnt)