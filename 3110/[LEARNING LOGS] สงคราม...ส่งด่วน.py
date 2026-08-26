"""kkk"""

start, end = input().upper().split()
weight = float(input())

if start == "BKK" and end == "CNX":
    price = 10 + (30 * weight)
    print(f"{price:.2f}")
elif start == "CNX" and end == "UBP":
    price = 15 + (40 * weight)
    print(f"{price:.2f}")
elif start == "UBP" and end == "BKK":
    price = 20 + (40 * weight)
    print(f"{price:.2f}")
elif start == "BKK" and end == "PKT":
    price = 25 + (50 * weight)
    print(f"{price:.2f}")
elif start == "PKT" and end == "CNX":
    price = 30 + (60 * weight)
    print(f"{price:.2f}")
elif start == "UBP" and end == "PKT":
    price = 40 + (70 * weight)
    print(f"{price:.2f}")
else:
    print("Error")
