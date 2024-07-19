from itertools import product

N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
print('\n'.join(map(' '.join, product(map(str, nums), repeat=M))))

