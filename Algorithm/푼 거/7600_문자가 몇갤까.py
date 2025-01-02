import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    cnt = set()

    s = input()
    if s == '#':
        break

    for i in s.lower():
        if i.isalpha():
            cnt.add(i)

    print(len(cnt))
