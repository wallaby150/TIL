import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
todos = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (-x[1], -x[0]))
time = [False] * (todos[0][1] + 1)


def solve():
    last = 1000001

    for todo in todos:
        t, s = todo
        for i in range(min(s, last-1), min(s, last-1)-t, -1):
            if time[i]:
                return -1
            time[i] = True
        else:
            last = i
    else:
        return time.index(True) - 1


print(solve())
