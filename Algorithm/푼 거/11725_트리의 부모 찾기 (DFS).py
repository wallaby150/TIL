import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = [0] * (N + 1)

stack = deque([1])
while stack:
    p = stack.pop()
    for num in tree[p]:
        if not answer[num]:
            answer[num] = p
            stack.append(num)

for a in answer[2:]:
    print(a)
