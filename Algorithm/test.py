import sys
input = lambda : sys.stdin.readline().rstrip()

# 게임 횟수, 이긴 게임
X, Y = map(int, input().split())
Z = int(Y / X * 100)


def solve(x, y, z):
    if z >= 99:
        return -1

    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        if int((y + mid) / (x + mid) * 100) >= z:
            end = mid - 1
        else:
            start = mid + 1

    return mid


print(solve(X, Y, Z))

