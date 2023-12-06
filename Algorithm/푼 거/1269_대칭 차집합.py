import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
answer = M - N + len(A - B) * 2
print(answer)