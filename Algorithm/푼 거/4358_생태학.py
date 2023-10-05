import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

trees = defaultdict(int)
count = 0

while True:
    tree = input()
    if tree == '':
        break

    trees[tree] += 1
    count += 1

trees_list = sorted(trees.items())

for t in trees_list:
    print(f'{t[0]} {t[1] / count * 100:.4f}')