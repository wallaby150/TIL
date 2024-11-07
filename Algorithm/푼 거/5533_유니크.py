import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
score = [[], [], []]
ans = []

for i in range(N):
    a, b, c = map(int, input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

freq = [{}, {}, {}]

for j in range(3):
    for num in score[j]:
        if num in freq[j]:
            freq[j][num] += 1
        else:
            freq[j][num] = 1

for i in range(N):
    tmp = 0
    for j in range(3):
        if freq[j][score[j][i]] == 1:
            tmp += score[j][i]
    ans.append(tmp)

for num in ans:
    print(num)