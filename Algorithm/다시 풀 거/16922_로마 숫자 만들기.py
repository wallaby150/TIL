import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = [1, 5, 10, 50]
tmp = []
ans = set()

def solve(idx, depth):
    if depth == N:
        ans.add(sum(tmp))
        return

    for i in range(idx, 4):
        tmp.append(nums[i])
        solve(i, depth + 1)
        tmp.pop()

solve(0, 0)
print(len(ans))