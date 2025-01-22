import sys
input = lambda: sys.stdin.readline().rstrip()

while 1:
    b = input()
    if b == '#':
        break
    cnt = b.count('1')
    last = b[-1]
    if 'e' == last:
        if cnt % 2 == 0:
            b = b.replace('e', '0')
        else:
            b = b.replace('e', '1')
    elif 'o' == last:
        if cnt % 2 == 0:
            b = b.replace('o', '1')
        else:
            b = b.replace('o', '0')
    print(b)
