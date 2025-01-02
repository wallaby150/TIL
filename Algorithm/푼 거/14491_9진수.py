t = int(input())
ans = ""

while t > 0:
    ans += str(t % 9)
    t //= 9
    
print(ans[::-1])