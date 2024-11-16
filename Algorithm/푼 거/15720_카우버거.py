B, C, D = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

total = sum(burgers) + sum(sides) + sum(drinks)
print(total)
for i in range(min(len(burgers), len(sides), len(drinks))):
    now = (burgers[i] + sides[i] + drinks[i])
    total -= now // 10

print(total)