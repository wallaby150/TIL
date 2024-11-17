N = int(input())
now = 10

while N > now:
    if N % now >= now // 2:
        N += now
    N -= (N % now)
    now *= 10

print(N)
