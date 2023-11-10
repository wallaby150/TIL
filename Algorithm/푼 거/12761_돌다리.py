from collections import deque

A, B, N, M = map(int, input().split())
stone = [-1] * 100001
stone[N] = 0
q = deque([N])

while q:
    num = q.popleft()
    if num == M:
        print(stone[M])
        break

    for jump in [1, A, B]:
        togo_list = []
        togo_list.append(num + jump)
        togo_list.append(num * jump)
        togo_list.append(num - jump)

        for togo in togo_list:
            if 0 <= togo < 100001 and stone[togo] == -1:
                stone[togo] = stone[num] + 1
                q.append(togo)

