import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    text = input()
    if text == '0':
        break

    nums = list(map(int, text.split()))
    ans = [nums[1]]
    tmp = set()

    for num in nums[2:]:
        if num != ans[-1]:
            ans.append(num)

    if ans:
        print(' '.join(map(str, ans)), '$')
