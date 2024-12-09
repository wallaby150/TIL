def solve():
    n = 0
    for i in range(3, 0, -1):
        x = input()
        if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
            n = int(x) + i

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


print(solve())
