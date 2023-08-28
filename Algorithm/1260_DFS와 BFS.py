import sys
from collections import deque
sys.stdin = open("1260_DFS와 BFS.txt")


def DFS(start):
    stack = [start]
    visited = [0] * (N+1)
    # visited[start] = 1
    road = []

    while stack:
        now = stack.pop()
        # # 요걸 깜빡했음
        # break
        if visited[now] == 1:
            continue
        visited[now] = 1
        road.append(now)
        a = sorted(maps[now], reverse=True)
        for v in a:
            if visited[v] == 0:
                stack.append(v)
    return road


def BFS(start):
    q = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1
    road = [start]

    while q:
        now = q.popleft()
        a = sorted(maps[now])
        for v in a:
            if visited[v] == 0:
                visited[v] = 1
                road.append(v)
                q.append(v)
    return road


for _ in range(int(input())):
    # 정점, 간선, 시작 번호
    N, M, V = map(int, input().split())
    maps = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        maps[a].append(b)
        maps[b].append(a)

    print(*DFS(V))
    print(*BFS(V))




'''
TC1
1 2 4 3
1 2 3 4

TC2
3 1 2 5 4
3 1 4 2 5

TC3
1000 999
1000 999

TC4
1 2 3 4
1 2 3 4

TC5
3 1 2 6 4 5 7
3 1 4 2 6 5 7
'''