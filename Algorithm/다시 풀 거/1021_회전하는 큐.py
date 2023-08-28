from collections import deque

# del, insert로도 풀어보기

# N은 큐의 크기, M은 뽑아내려고 하는 수의 개수
N, M = map(int, input().split())
targets = deque(list(map(int, input().split())))

q = deque([i for i in range(1, N+1)])
count = 0

while targets:
    target = targets.popleft()

    if q.index(target) >= len(q)/2:
        direction = "right"
    else:
        direction = "left"

    if direction == "right":
        while q[0] != target:
            q.appendleft(q.pop())
            count += 1
        else:
            q.popleft()
    # 왼쪽일 때
    else:
        while q[0] != target:
            q.append(q.popleft())
            count += 1
        else:
            q.popleft()

print(count)


