import sys
input = lambda : sys.stdin.readline().rstrip()

text = input()
ans = [0] * 10

for i in range(len(text)):
    num = int(text[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

print(max(ans))