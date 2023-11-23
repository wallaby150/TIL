import sys

input = lambda: sys.stdin.readline().rstrip()

# 세로, 가로, 연산 수
N, M, R = map(int, input().split())
array = list(list(map(int, input().split())) for _ in range(N))

orders = list(map(int, input().split()))

stack = []

for order in orders:
    # 처음이 아니라면
    if stack:
        last = stack[-1]

        # 2번해서 0이 되는 거라면
        if last == order and order in (1, 2):
            stack.pop()

        elif order == 3 and last == 4 or order == 4 and last == 3:
            stack.pop()

        elif order == 5 and last == 6 or order == 6 and last == 5:
            stack.pop()

        else:
            stack.append(order)

    # 처음이라면
    else:
        stack.append(order)


def do1():
    global array
    array = array[::-1]
    return


def do2():
    global array
    tmp = []
    for line in array:
        tmp.append(line[::-1])
    array = tmp
    return


def do3():
    global array
    tmp = []
    for x in range(M):
        line = []
        for y in range(N - 1, -1, -1):
            line.append(array[y][x])
        tmp.append(line)
    array = tmp
    return


def do4():
    global array
    tmp = []
    for x in range(M - 1, -1, -1):
        line = []
        for y in range(N):
            line.append(array[y][x])
        tmp.append(line)
    array = tmp
    return


def do5():
    global array
    half_y = N // 2
    half_x = M // 2

    one = []
    two = []
    three = []
    four = []

    for y in range(N):
        left = []
        right = []
        for x in range(M):
            if x < half_x:
                left.append(array[y][x])
            else:
                right.append(array[y][x])

        if y < half_y:
            one.append(left)
            two.append(right)
        else:
            three.append(right)
            four.append(left)

    tmp = []

    for y in range(N):
        line = []

        if y < half_y:
            line += four[y]
            line += one[y]
            tmp.append(line)

        else:
            line += three[y - half_y]
            line += two[y - half_y]
            tmp.append(line)

    array = tmp
    return


def do6():
    global array
    half_y = N // 2
    half_x = M // 2

    one = []
    two = []
    three = []
    four = []

    for y in range(N):
        left = []
        right = []
        for x in range(M):
            if x < half_x:
                left.append(array[y][x])
            else:
                right.append(array[y][x])

        if y < half_y:
            one.append(left)
            two.append(right)
        else:
            three.append(right)
            four.append(left)

    tmp = []

    for y in range(N):
        line = []

        if y < half_y:
            line += two[y]
            line += three[y]
            tmp.append(line)

        else:
            line += one[y - half_y]
            line += four[y - half_y]
            tmp.append(line)

    array = tmp
    return


def solve(o):
    global N, M
    if o == 1:
        do1()
    elif o == 2:
        do2()
    elif o == 3:
        do3()
        N, M = M, N
    elif o == 4:
        do4()
        N, M = M, N
    elif o == 5:
        do5()
    else:
        do6()


for o in stack:
    solve(o)

for line in array:
    print(*line)
