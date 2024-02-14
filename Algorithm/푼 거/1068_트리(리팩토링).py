import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N)]
parent = list(map(int, input().split()))
x = int(input())

# i는 자식 번호
for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        # 지울 애들은 아예 추가 x
        if i != x and parent[i] != x:
            tree[parent[i]].append(i)

if x == root:
    print(0)
else:
    stack = tree[root][:]
    # 루트 노드가 리프 노드일 때
    if not stack:
        cnt = 1
    else:
        cnt = 0
        while stack:
            node = stack.pop()
            tmp = tree[node]

            if len(tmp) == 0:
                cnt += 1
            else:
                stack.extend(tmp)

    print(cnt)