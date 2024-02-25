import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
visited = [0] * 1001
nums = [1, 5, 10, 50]
tmp = []

def solve(idx, depth):
    if depth == N:
        visited[sum(tmp)] = 1
        return

    for i in range(idx, 4):
        tmp.append(nums[i])
        solve(idx, depth + 1)
        tmp.pop()

solve(0, 0)
print(sum(tmp))