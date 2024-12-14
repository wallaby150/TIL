import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    order = sorted(nums, reverse=True)
    total = sum(nums)

    if order[0] == order[1]:
        print("no winner")
    else:
        if order[0] >= total // 2 + 1:
            print(f"majority winner {nums.index(order[0]) + 1}")
        else:
            print(f"minority winner {nums.index(order[0]) + 1}")
