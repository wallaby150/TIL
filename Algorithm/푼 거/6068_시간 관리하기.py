import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
todos = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: -x[1])

last = todos[0][1]
for i in range(N):
    todo = todos[i]
    if todo[1] <= last:
        last = todo[1] - todo[0]
    else:
        last -= todo[0]

if last >= 0:
    print(last)
else:
    print(-1)
