N = int(input())
nums = sorted(list(set(map(int, input().split()))))
print(*nums)