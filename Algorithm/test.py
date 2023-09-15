import sys, re
input = lambda : sys.stdin.readline().rstrip()

p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    print('Good' if p.match(input())==None else 'Infected!')