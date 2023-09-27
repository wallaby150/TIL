import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
s = [0]
tmp = 0

for num in nums:
    tmp += num
    s.append(tmp)

for _ in range(int(input())):
    start, end = map(int, input().split())
    print(s[end] - s[start-1])