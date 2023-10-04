import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
kids = list(map(int, input().split()))
gaps = []

for i in range(1, N):
    gaps.append(kids[i] - kids[i-1])

gaps.sort(reverse=True)
print(sum(gaps[K-1:]))