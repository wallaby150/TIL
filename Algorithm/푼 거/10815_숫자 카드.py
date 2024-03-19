import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
card = list(map(int, input().split()))
M = int(input())
x = list(map(int, input().split()))

d = {}
for i in range(N):
    d[card[i]] = True

for i in x:
    if i in d:
        print(1, end=" ")
    else:
        print(0, end=" ")
