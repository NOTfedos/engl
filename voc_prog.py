from random import randint, sample

f = open("vocab_dict_tr.txt", "r", encoding="utf-8")

words = dict()
rest = dict()
for line in f:
    if line[0] != "-":
        eng, rus = line.replace("\n", "").split("; ")
        eng = eng.strip()
        rus = rus.strip()
        words.update({eng: rus})

print("Data loaded, starts exam")

k = 0
right = 0
k_end = len(words.keys())
iter = 0


for eng, rus in sample(words.items(), k_end):
    k += 1
    print(f"--------------------------- {k} / {k_end} ------------------------------------")
    if randint(0, 0) == 0:
        # print(f"{k} / {k_end}: {rus}, your translate is ", end='')
        ans = input(f"{k} ({right} / {k_end}): {rus}, your translate is ")
        if ans.lower() == eng.lower():
            right += 1
            print("RIGHT")
        else:
            rest.update({eng: rus})
            print(f"WRONG, translate is {eng}")
    else:
        # print(f"{k} / {k_end}: {eng}, your translate is ", end='')
        ans = input(f"{k} ({right} / {k_end}): {eng}, your translate is ")
        if ans.lower() == rus.lower():
            right += 1
            print("RIGHT")
        else:
            rest.update({eng: rus})
            print(f"WRONG, translate is {rus}")

print("--------------------------------------------------------------------")
print("Now lest deal with remain words")

while len(rest.keys()) != 0:
    k = 0
    right = 0
    k_end = len(rest.keys())
    new_rest = dict()
    print("---------------------------RESOLVING-------------------------------------")
    for eng, rus in rest.items():
        k += 1
        print(f"--------------------------- {k} / {k_end} ------------------------------------")
        if randint(0, 0) == 0:
            # print(f"{k} / {k_end}: {rus}, your translate is ", end='')
            ans = input(f"{k} ({right} / {k_end}): {rus}, your translate is ")
            if ans.lower() == eng.lower():
                right += 1
                print("RIGHT")
            else:
                print(f"WRONG, translate is {eng}")
                new_rest.update({eng: rus})
        else:
            # print(f"{k} / {k_end}: {eng}, your translate is ", end='')
            ans = input(f"{k} ({right} / {k_end}): {eng}, your translate is ")
            if ans.lower() == rus.lower():
                right += 1
                print("RIGHT")
            else:
                print(f"WRONG, translate is {rus}")
                new_rest.update({eng: rus})
    rest = new_rest.copy()

print("That's all")
