ans = 0

for _ in range(10):
    num = int(input())

    if abs(100 - ans - num) <= 100 - ans:
        ans += num
    else:
        break

print(ans)