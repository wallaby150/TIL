import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
texts = list(input().split())
first = texts[0][0]

for text in texts:
    if text[0] != first:
        print(0)
        break
else:
    print(1)