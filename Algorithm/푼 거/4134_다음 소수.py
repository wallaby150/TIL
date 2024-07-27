import sys
input = lambda: sys.stdin.readline().rstrip()


def check(x):
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True


T = int(input())
for i in range(T):
    n = int(input())

    if n == 0 or n == 1:
        print(2)
    else:
        while True:
            if check(n):
                print(n)
                break
            else:
                n += 1
