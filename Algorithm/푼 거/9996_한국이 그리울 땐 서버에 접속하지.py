import sys, re
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
pattern = list(input().split('*'))
c = re.compile(pattern[0]+'.*'+pattern[1])

for _ in range(N):
    text = input()
    if c.fullmatch(text):
        print('DA')
    else:
        print('NE')
