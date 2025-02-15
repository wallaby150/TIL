import math

a, b, c = map(int, input().split())
ans = math.floor(max(a*b/c, a/b*c))
print(ans)