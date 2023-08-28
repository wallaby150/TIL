from collections import deque


def bfs(num):
    q = deque([num])
    while q:
        num = q.popleft()
        if num == K:
            return array[K]

        for next_num in [num-1, num+1, num*2]:
            if 0 <= next_num < max_num and not array[next_num]:
                array[next_num] = array[num] + 1
                q.append(next_num)


N, K = map(int, input().split())
max_num = 100001
array = [0] * max_num
print(bfs(N))
