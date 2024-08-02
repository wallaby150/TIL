import sys
input = lambda : sys.stdin.readline().rstrip()

text = input()
L = len(text)
Q = int(input())
ans = 0
hap = {}
alphabets = 'abcdefghijklmnopqrstuvwxyz'

for alphabet in alphabets:
    hap[alphabet] = [0] * (L + 1)

for i in range(L):
    for alpha in alphabets:
        hap[alpha][i+1] = hap[alpha][i]
        if alpha == text[i]:
            hap[alpha][i+1] += 1

for _ in range(Q):
    char, l, r = input().split()
    l, r = int(l), int(r)
    print(hap[char][r+1] - hap[char][l])
