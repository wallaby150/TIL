import sys
input = lambda : sys.stdin.readline().rstrip()

cocktails = list(map(int, input().split()))
odd = 1
even = 1
flag = False

for c in cocktails:
    # 홀수면
    if c % 2:
        odd *= c
        flag = True
    else:
        even *= c

if flag:
    print(odd)
else:
    print(even)