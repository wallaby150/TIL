import sys
input = lambda : sys.stdin.readline().rstrip()

k = int(input())
x = '01'
count = 0
tmp = 2

while k >= 3:
    if k <= tmp * 2:
        k -= tmp
        count += 1
        tmp = 2
    else:
        tmp *= 2

# 반전횟수가 홀수면
if count % 2:
    ans = not int(x[k-1])
else:
    ans = int(x[k-1])

if ans:
    print(1)
else:
    print(0)