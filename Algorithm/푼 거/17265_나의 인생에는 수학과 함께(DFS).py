import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
# 최대값, 최소값
high, low = -626, 3126
greed = list(list(input().split()) for _ in range(N))


def check(line):
    global high, low

    tmp = line[0]
    for i in range(1, len(line), 2):
        tmp += line[i:i+2]
        tmp = str(eval(tmp))
    tmp = int(tmp)
    high = max(high, tmp)
    low = min(low, tmp)
    return


def move(y, x, now):
    now += greed[y][x]

    if y == x == N-1:
        check(now)
        return

    for ny, nx in ((y+1, x), (y, x+1)):
        if ny < N and nx < N:
           move(ny, nx, now)


move(0, 0, '')
print(high, low)