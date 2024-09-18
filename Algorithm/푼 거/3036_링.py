def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
rings = list(map(int, input().split()))

first_ring = rings[0]

for ring in rings[1:]:
    common_divisor = gcd(first_ring, ring)
    numerator = first_ring // common_divisor
    denominator = ring // common_divisor
    print(f"{numerator}/{denominator}")