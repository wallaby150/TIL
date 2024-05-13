import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
L = int(input())
nums = list(map(int, input().split()))

visited = [0] * 101
order = []

for num in nums:
    if num in order:
        visited[num] += 1

    # 목록에 없다면
    else:
        # 아직 꽉 안 찼을 때
        if len(order) < N:
            visited[num] = 1
            order.append(num)

        # 꽉 차있다면
        else:
            tmp = (0, 1000)
            for candi in order:
                if visited[candi] < tmp[1]:
                    tmp = (candi, visited[candi])

            visited[tmp[0]] = 0
            visited[num] = 1

            order.remove(tmp[0])
            order.append(num)

print(*sorted(order))
