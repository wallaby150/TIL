import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
# +, -, X, /
cals = list(map(int, input().split()))
high, low = -1000000001, 1000000001
cal_dict = {}


def calculate():
    global high, low

    count = 0
    stack = list(cal_dict.items())
    stack.sort(key=lambda x: x[1] > 1, reverse=True)
    now_nums = nums[:]

    for data in stack:
        index = max(0, data[0] - count)
        cal = data[1]

        if cal == 0:
            now_nums[index] += now_nums[index + 1]
        elif cal == 1:
            now_nums[index] -= now_nums[index + 1]
        elif cal == 2:
            now_nums[index] *= now_nums[index + 1]
        else:
            now_nums[index] = int(now_nums[index] / now_nums[index + 1])
        if len(now_nums) > 1:
            del now_nums[index + 1]
        count += 1

    answer = now_nums[0]
    high = max(high, answer)
    low = min(low, answer)
    return


def solve(index):
    global high, low

    if index == N - 1:
        calculate()
        return

    for i in range(4):
        if cals[i]:
            cals[i] -= 1
            cal_dict[index] = i
            solve(index + 1)
            del cal_dict[index]
            cals[i] += 1


solve(0)

print(high)
print(low)
