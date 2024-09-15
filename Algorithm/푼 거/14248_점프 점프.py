import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
now = int(input())

visited = [False] * N
visited[now - 1] = True
stack = [now - 1]

while stack:
    nn = stack.pop()
    for togo in [nn - nums[nn], nn + nums[nn]]:
        if 0 <= togo < N and not visited[togo]:
            visited[togo] = True
            stack.append(togo)

print(sum(visited))