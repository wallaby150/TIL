import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
settable_list = list(map(int, input().split()))

road = [0] * N
ans = 1000000

for i in range(1, 100001):
    for light in settable_list:
        if 0 in road[max(0, light-i):light+i]:
            for j in range(max(0, light-i), min(light+i, N)):
                road[j] = 1

    if 0 not in road:
        ans = i
        break


print(i)
