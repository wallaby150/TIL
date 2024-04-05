import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
tmp = set()
cnt = 0

for _ in range(N):
    text = input()

    if text not in tmp:
        cnt += 1
        for i in range(len(text)):
            tmp.add(text[i:]+text[:i])

print(cnt)