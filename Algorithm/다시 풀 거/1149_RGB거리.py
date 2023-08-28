import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
price_list = list(list(map(int, input().split())) for _ in range(N))
lowerest = 1000001

# 지금 가격과 이전 색깔을 넘긴다.
def paint(now_price, old, count):
    global lowerest
    colors = "RGB"

    if count == N:
        lowerest = min(lowerest, now_price)
        return

    for i in range(3):
        if colors[i] != old:
            paint(now_price + price_list[count][i], colors[i], count+1)


paint(0, "", 0)

print(lowerest)