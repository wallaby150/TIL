import sys

def find_duplicate():
    n = int(input())
    numbers = map(int, sys.stdin.read().split())

    expected_sum = (n - 1) * n // 2
    actual_sum = sum(numbers)

    return actual_sum - expected_sum

print(find_duplicate())
