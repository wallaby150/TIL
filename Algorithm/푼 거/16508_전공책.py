import sys
input = lambda: sys.stdin.readline().rstrip()

books = []
count = [0] * 26
select = [0] * 26
min_price = float('inf')

text = input()
N = int(input())

for char in text:
    count[ord(char) - ord('A')] += 1

for _ in range(N):
    price, title = input().split()
    books.append((int(price), title))


def dfs(idx, total):
    global min_price
    if idx == N:
        if check():
            min_price = min(total, min_price)
        return
    if total > min_price:
        return

    for char in books[idx][1]:
        select[ord(char) - ord('A')] += 1
    dfs(idx + 1, total + books[idx][0])

    for char in books[idx][1]:
        select[ord(char) - ord('A')] -= 1
    dfs(idx + 1, total)


def check():
    for i in range(26):
        if count[i] > select[i]:
            return False
    return True


dfs(0, 0)
print(-1 if min_price == float('inf') else min_price)
