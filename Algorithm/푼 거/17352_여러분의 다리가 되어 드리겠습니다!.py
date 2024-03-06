import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()


N = int(input())
if N == 2:
    print(1, 2)
else:
    visited = [0] * (N + 1)
    visited[0] = 1
    graph = defaultdict(list)

    for _ in range(N-2):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    stack = graph.get(1)
    visited[1] = 1

    while stack:
        num = stack.pop()
        visited[num] = 1
        for togo in graph[num]:
            if visited[togo] == 0:
                stack.append(togo)

    print(1, visited.index(0))

