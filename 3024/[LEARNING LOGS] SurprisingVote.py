"""WOW_So_Surprising"""

total = float(input())
high = float(input())

min_num = max(0, total - 2 * high)

if high - min_num > 2.0:
    print("Surprising")
else:
    print("Not surprising")
