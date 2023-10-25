import sys
input = lambda: sys.stdin.readline().rstrip()

# 스위치의 수, 램프의 수 M
N, M = map(int, input().split())
lamps = [0] * M
c_list = []

for _ in range(N):
    connects = list(map(int,input().split()))[1:]
    c_list.append(connects)

    for i in connects:
        lamps[i-1] += 1

c_list.sort(key=lambda x: len(x))

for c in c_list:
    for j in c:
        if lamps[j-1] < 2:
            break
    else:
        print(1)
        break
else:
    print(0)
