import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
connect_N = int(input())
computers = list([0] * (N+1) for _ in range(N+1))

# 연결 표시하기
for _ in range(connect_N):
    a, b = map(int, input().split())
    computers[a][b] = 1
    computers[b][a] = 1

visited = [0] * (N+1)
visited[1] = 1
stack = [1]

while stack:
    now = stack.pop()
    for i in range(1, N+1):
        if computers[now][i] == 1 and visited[i] == 0:
            visited[i] = 1
            stack.append(i)

print(visited.count(1)-1)

