N = int(input()) - 1
x, y = N // 14, N % 14
dict =  {0 : 'baby',
         1 : 'sukhwan',
         4 : 'very',
         5 : 'cute',
         8 : 'in',
         9 : 'bed',
         12 : 'baby',
         13 : 'sukhwan'}

if y in dict:
    print(dict[y])
else:
    cnt = (y % 2) * -1 + 2 + x
    if cnt >= 5:
        print(f"tu+ru*{cnt}")
    else:
        print("tu"+"ru"*cnt)