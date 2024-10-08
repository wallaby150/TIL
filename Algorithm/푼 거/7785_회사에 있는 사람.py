import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
company = set()

for _ in range(N):
    name, move = input().split()
    if move == 'enter':
        company.add(name)
    else:
        company.remove(name)

for man in sorted(list(company), reverse=True):
    print(man)