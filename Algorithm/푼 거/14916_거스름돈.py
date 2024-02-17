N = int(input())

def solve():
    for i in range(N//5, -1, -1):
        rest = N - 5 * i
        for j in range(rest//2, -1, -1):
            tmp = rest - 2 * j
            if tmp == 0:
                return(i + j)
    return -1

print(solve())