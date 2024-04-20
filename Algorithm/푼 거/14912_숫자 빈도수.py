import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = input().split()
print(str(list(range(1, int(N)+1))).count(M))