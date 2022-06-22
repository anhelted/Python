def ordinalNumber(num):
    ordinalDict = {1: "st", 2: "nd", 3: "rd"}
    x, mod = divmod(num, 10)
    suffix = x % 10 != 1 and ordinalDict.get(mod) or "th"
    print(f"{num}, '{suffix}'")

print("Ordinal Number")
print("type '0' to stop the program")

loop = True
while loop == True:
    num = int(input("Input Number : "))
    if num == 0:
        loop = False;
        break
    else:
        ordinalNumber(num)