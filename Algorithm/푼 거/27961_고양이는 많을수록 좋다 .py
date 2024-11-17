N = int(input())
cnt, cat = 1, 1
if N == 0:
    print(0)
else:
    while cat < N:
        cat *= 2
        cnt += 1
    print(cnt)