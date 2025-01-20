a, b = input().split()
low = int(a.replace('6', '5')) + int(b.replace('6', '5'))
high = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(low, high)