""""kkk"""

text = input().lower()

char = ["a","e","i","o","u"]

for ch in char:
    x = text.count(ch)
    if x > 0:
        print(f"{ch} : {x}")
