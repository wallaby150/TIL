import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([[1, tree[1][:]]])
visited = [False] * (N + 1)
answer = [0] * (N + 1)

while q:
    num, togos = q.popleft()
    for togo in togos:
        if not visited[togo]:
            visited[togo] = True
            q.append([togo, tree[togo][:]])
            answer[togo] = num

for a in answer[2:]:
    print(a)