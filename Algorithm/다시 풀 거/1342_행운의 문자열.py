import sys
input = lambda : sys.stdin.readline().rstrip()

# 다음에는 DFS로 풀어보기

text = input()
ans = 0
a = list(text)

def solve(i, now, rest):
    global ans

    if rest == []:
        ans += 1
        return

    # 만약 처음이라면
    if i == 0:
        for char in set(rest):
            temp = rest[:]
            temp.remove(char)
            solve(1, char, temp)
    else:
        temp = set(rest)
        temp.discard(now[-1])
        for char in temp:
            t = rest[:]
            t.remove(char)
            solve(i+1, now+char, t)

solve(0, '', a)
print(ans)