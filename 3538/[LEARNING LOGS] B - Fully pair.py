"""kkk"""

text = input()

LIST = []

for i in text:
    x = text.count(i)
    if x % 2 :
        LIST.append(i)

LIST = list(dict.fromkeys(LIST))

if not LIST:
    print("fully paired")
else:
    for j in LIST:
        print(j, end="")
