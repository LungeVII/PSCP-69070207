
"""kkk"""

material = ["Pad Thai Sauce",
            "Tofu",
            "Pickle Turnip",
            "Shrimp",
            "Bean Sprouts",
            "Noodle",
            "Chives",
            "Lime",
            "Egg",
            "Oil",
            "Peanuts"]

favor = ["Sweet", "Sour", "Salty"]

LIST1 = []
while True:
    text1 = input()
    if text1 == "Cook":
        break
    LIST1.append(text1)

LIST2 = []
while True:
    text2 = input()
    if text2 == "End":
        break
    LIST2.append(text2)

bad_material = False

for i in LIST1:
    if i not in material:
        bad_material = True

if bad_material:
    print("This is not Pad Thai!!!")
else:
    for i in LIST1:
        if i in material:
            material.remove(i)

    if material:
        print("This is bad!")
    else:
        bad_favor = False

        for j in LIST2:
            if j not in favor:
                bad_favor = True

        for j in LIST2:
            if j in favor:
                favor.remove(j)

        if bad_favor or favor:
            print("Not Bad...")
        else:
            print("Delicious!")
