import sys, math
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

visited = [False, False] + [True] * 1003010
for i in range(2, int(math.sqrt(1003011))+1):
    if visited[i] == True:
        for j in range(i * 2, 1003011, i):
            visited[j] = False

for k in range(N, 1003002):
    if visited[k]:
        if str(k) == str(k)[::-1]:
            print(k)
            break

