N = int(input())
temp = [0] * 1001

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    temp[1] = 1
    temp[2] = 2
    for idx in range(3, N+1):
        temp[idx] = temp[idx-1] + temp[idx-2]
    print(temp[N] % 10007)

