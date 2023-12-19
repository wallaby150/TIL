import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
q = int(n ** 0.5)
if q ** 2 < n:
    q += 1
print(q)
