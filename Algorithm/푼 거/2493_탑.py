import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
ans = [0] * N
stack = []

for i in range(N-1, -1, -1):
    num = nums[i]

    while stack:
        idx, value = stack.pop()
        if num >= value:
            ans[idx] = i + 1
        else:
            stack.append((idx, value))
            break
    stack.append((i, num))

print(*ans)
