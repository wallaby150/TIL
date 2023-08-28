# 목표 숫자, 최소 길이
N, L = map(int, input().split())
sums_list = [0, 1]

for i in range(2, 101):
    sums_list.append(sums_list[i-1]+i)

# print(sums_list)

for j in range(L, 101):
    if sums_list[j-1] > N:
        print(-1)
        break

    num = (N-sums_list[j-1]) / j
    if num == int(num):
        for ans in range(int(num), int(num)+j):
            print(ans, end=" ")
        break
else:
    print(-1)

