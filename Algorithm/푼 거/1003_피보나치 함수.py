def fibonacci(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        else:
            fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]


T = int(input())
fibo_list = list(0 for _ in range(41))
fibo_list[1] = 1
fibonacci(40)

for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, fibo_list[N])
    else:
        print(fibo_list[N-1], fibo_list[N])