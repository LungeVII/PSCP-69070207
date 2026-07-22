"""kkkk"""
price = int(input())

if price <500:
    x = price + 50
    y = x+(x*7/100)
    print(f"{y:.2f}")
elif price >10000:
    x = price + 1000
    y = x+(x*7/100)
    print(f"{y:.2f}")
else:
    x = price + (price*10/100)
    y = x+(x*7/100)
    print(f"{y:.2f}")
