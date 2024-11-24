def digit_sum(num, base):
    total = 0
    while num > 0:
        total += num % base
        num //= base
    return total


for num in range(1000, 10000):
    sum_10 = digit_sum(num, 10)
    sum_12 = digit_sum(num, 12)
    sum_16 = digit_sum(num, 16)

    if sum_10 == sum_12 == sum_16:
        print(num)