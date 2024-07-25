import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [input() for _ in range(N)]


def sum_num(text):
    result = 0
    for char in text:
        if char.isdigit():
            result += int(char)
    return result


arr.sort(key=lambda x: (len(x), sum_num(x), x))
for i in arr:
    print(i)
