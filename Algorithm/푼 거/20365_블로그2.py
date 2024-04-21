N = int(input())
text = input() + 'X'
cnt = {'B': 0, 'R': 0}
last = text[0]

for i in range(N+1):
    if text[i] != last:
        cnt[last] += 1
        last = text[i]

print(min(cnt.values()) + 1)
