import sys
# from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
# +, -, X, /
cal = list(map(int, input().split()))
high, low = -1000000001, 1000000001
cal_dict = {}


def Calculate():
    count = 0
    stack = list(cal_dict.items())
    stack.sort(key=lambda x: x[1] > 1, reverse=True)
    print(stack)

def solve(index):
    global high, low

    if index == N - 1:
        Calculate()
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            cal_dict[index] = i
            solve(index + 1)
            del cal_dict[index]
            cal[i] += 1


solve(0)




# print(high)
# print(low)