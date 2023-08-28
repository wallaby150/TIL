import sys
input = lambda : sys.stdin.readline().rstrip()

A, B = map(str, input().split())

count = 51
for start in range(len(B)-len(A)+1):
    temp = 0
    for now in range(len(A)):
        if B[start+now] != A[now]:
            temp += 1
    count = min(temp, count)

print(count)