import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
q = deque([])

for _ in range(N):
    order = input()
    if order == 'size':
        print(len(q))
    elif order == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    else:
        temp = list(map(str, order.split()))
        num = temp[1]
        q.append(int(num))