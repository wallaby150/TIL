import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

start = 1
end = 1
tmp = 1
count = 0

while end <= N:
    if tmp == N:
        count += 1
        tmp -= start
        start += 1

    elif tmp < N:
        end += 1
        tmp += end

    else:
        tmp -= start
        start += 1

print(count)