
"""kkk"""

import json

data = {}
dead = {}

while True:
    text = input()

    if text == "Start":
        break

    x = json.loads(text)
    data.update(x)

while True:
    text = input()

    if text == "End":
        break

    if text in data:
        dead[text] = data.pop(text)

count = 0

for role in data.values():
    if role == "Impostor":
        count += 1

print(f"{count} Impostor Remains")
print("***Alive***")

for name in sorted(data):
    print(name, ":", data[name])

print("***Dead***")

for name in sorted(dead):
    print(name, ":", dead[name])
