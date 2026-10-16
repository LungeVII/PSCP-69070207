"""kkk"""

import json

N = int(input())
DICT = {}

for _ in range(N):
    data = json.loads(input())
    DICT.update(data)

if "Cat01" not in DICT.values() and "Garfield" not in DICT:
    DICT.update({"Garfield": "Cat01"})

if "Fox01" not in DICT.values() and "Fubuki" not in DICT:
    DICT.update({"Fubuki": "Fox01"})

cat = 0
fox = 0

for number in DICT.values():
    if number[0:3] == "Cat":
        cat += 1
    else:
        fox += 1

cats = []
foxs = []

for name, number in DICT.items():
    if number[0:3] == "Cat":
        cats.append([name, number])
    else:
        foxs.append([name, number])

sort_cats = []
sort_foxs = []

while cats:
    min_num = 999
    min_index = 0

    for j, cat_data in enumerate(cats):
        num = int(cat_data[1][3:])

        if num < min_num:
            min_num = num
            min_index = j

    sort_cats.append(cats[min_index])
    cats.pop(min_index)

while foxs:
    min_num = 999
    min_index = 0

    for j, fox_data in enumerate(foxs):
        num = int(fox_data[1][3:])

        if num < min_num:
            min_num = num
            min_index = j

    sort_foxs.append(foxs[min_index])
    foxs.pop(min_index)

print(f"Cat : {cat}")
print(f"Fox : {fox}")

for name, number in sort_cats:
    print(f"{name} : {number}")

for name, number in sort_foxs:
    print(f"{name} : {number}")
