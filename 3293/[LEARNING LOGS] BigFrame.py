"""kkk"""
text = []

for _ in range(5):
    text.append(input().rstrip())

max_len = max(len(x) for x in text)

print("*" * (max_len + 4))

for x in text:
    space = max_len - len(x)
    print("* " + x + " " * space + " *")

print("*" * (max_len + 4))
