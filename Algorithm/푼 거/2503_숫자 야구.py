import sys
from itertools import permutations
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(data, 3))

for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    tmp = []

    for i in range(len(num)):
        strike = ball = 0
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if strike == s and ball == b:
            tmp.append(num[i])

    num = tmp[:]

print(len(num))