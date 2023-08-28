# 달걀 수, 고객 수
N, M = map(int, input().split())
prices = list(int(input()) for i in range(M))
targets = sorted(prices, reverse=True)[:N]
ans = [0, 0]

highest_price = 0
highest_profit = 0


# 기준 가격
for value in targets:
    temp_sum = 0
    # 고객 한 명씩
    for target in targets:
        if target >= value:
            temp_sum += value
        else:
            break
    if highest_profit <= temp_sum:
        highest_price = value
        highest_profit = temp_sum

print(highest_price,highest_profit)
