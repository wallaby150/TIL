import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
positive = []
negative = []
zero = False
answer = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        zero = True
    elif num > 0:
        positive.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()
pl = len(positive)
nl = len(negative)

for i in range(0, nl, 2):
    num = negative[i]

    # 마지막 수라면
    if i == nl - 1:
        if zero:
            pass
        else:
            answer += num
        continue

    # 아니라면
    right = negative[i+1]
    answer += num * right

for j in range(0, pl, 2):
    num = positive[j]

    if j == pl - 1:
        answer += num
        continue

    left = positive[j+1]
    if left == 1:
        answer += num + left
    else:
        answer += num * left

print(answer)