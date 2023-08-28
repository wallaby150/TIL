T = int(input())

length_list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(T):
    N = int(input())
    while len(length_list) <= N:
        length_list.append(length_list[-1]+length_list[-5])
    print(length_list[N])
