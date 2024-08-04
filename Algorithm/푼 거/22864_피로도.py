A, B, C, M = map(int, input().split())
tired, work = 0, 0

for _ in range(24):
    # 번아웃이 올 거 같으면
    if tired + A > M:
        tired = max(0, tired-C)
    # 일할 수 있으면
    else:
        tired += A
        work += B

print(work)
