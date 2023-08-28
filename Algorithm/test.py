import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
price_list = sorted(list(int(input()) for _ in range(N)), reverse=True)
ans = sum(price_list)

print(price_list)
for i in range(2, len(price_list), 3):
    print(i)
    ans -= price_list[i]

print(ans)