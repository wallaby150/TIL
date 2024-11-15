arr = [i for i in range(1, 21)]

for i in range(10):
    m, n = map(int, input().split())
    arr = arr[:m - 1] + arr[m - 1:n][::-1] + arr[n:]

print(' '.join(map(str, arr)))