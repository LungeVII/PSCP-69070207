"""TEMP_CHANGE"""

temp = float(input())
char1 = input()
char2 = input()

if char1 == "C":
    c = temp
elif char1 == "F":
    c = (temp - 32) * 5 / 9
elif char1 == "K":
    c = temp - 273.15
else:
    c = (temp - 491.67) * 5 / 9

if char2 == "C":
    ans = c
elif char2 == "F":
    ans = c * 9 / 5 + 32
elif char2 == "K":
    ans = c + 273.15
else:
    ans = (c + 273.15) * 9 / 5

print(f"{ans:.2f}")
