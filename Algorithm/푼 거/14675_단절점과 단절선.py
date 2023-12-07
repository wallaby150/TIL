import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = list([] for _ in range(N+1))

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 2:
        print('yes')
    else:
        if len(tree[k]) == 1:
            print('no')
        else:
            print('yes')
