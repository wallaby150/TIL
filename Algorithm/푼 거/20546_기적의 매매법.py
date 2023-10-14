import sys
input = lambda: sys.stdin.readline().rstrip()

money = int(input())
chart = list(map(int, input().split()))

jh_money, sm_money = money, money
jh_stock, sm_stock = 0, 0

for day in range(14):
    price = chart[day]

    # JH의 거래
    if price <= jh_money:
        jh_stock += jh_money // price
        jh_money %= price

    # SM의 거래 (3일 연속 상승 또는 하락 확인)
    if day >= 3:
        if chart[day - 1] > chart[day - 2] > chart[day - 3]:
            sm_money += price * sm_stock
            sm_stock = 0
        elif chart[day - 1] < chart[day - 2] < chart[day - 3]:
            sm_stock += sm_money // price
            sm_money %= price

jh_total = jh_money + (jh_stock * chart[-1])
sm_total = sm_money + (sm_stock * chart[-1])

if jh_total == sm_total:
    print("SAMESAME")
elif jh_total > sm_total:
    print("BNP")
else:
    print("TIMING")
