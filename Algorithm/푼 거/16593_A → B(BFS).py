import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


A, B = map(int, input().split())
q = deque([[A, 0]])

while q:
    num, count = q.popleft()

    if num == B:
        print(count + 1)
        break

    twice, add_one = num * 2, num * 10 + 1
    if twice <= B:
        q.append([twice, count + 1])

    if add_one <= B:
        q.append([add_one, count + 1])


else:
    print(-1)