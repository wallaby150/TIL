import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
count = [0] * 26
select = [0] * 26
min_price = float('inf')


def dfs(depth, total):
    global min_price
    if depth == n:
        if check():
            min_price = min(total, min_price)
        return

    for char in arr[depth][1]:
        select[ord(char) - ord('A')] += 1
    dfs(depth + 1, total + arr[depth][0])

    for char in arr[depth][1]:
        select[ord(char) - ord('A')] -= 1
    dfs(depth + 1, total)

def check():
    for i in range(26):
        if count[i] > select[i]:
            return False
    return True


text = input()
n = int(input())

for char in text:
    count[ord(char) - ord('A')] += 1

for _ in range(n):
    price, title = input().split()
    arr.append((int(price), title))

dfs(0, 0)
print(-1 if min_price == float('inf') else min_price)
