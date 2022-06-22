total = 0
while True:
    try:
        age = int(input("Input Age : "))
    except ValueError:
        break
    if age <= 2:
        print("Free")
    elif age in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        total += 14.00
        print("Price $14.00")
        print(f"Running Total : ${total}")
    elif age >= 65:
        total += 18.00
        print("Price $18.00")
        print(f"Running Total : ${total}")
    else:
        total += 23.00
        print("Price $23.00")
        print(f"Running Total : ${total}")

money = int(input("Enter the amount of money : "))
if money > total:
    bayar = money - total
    print(f"Chane : ${bayar}")
elif money < total:
    bayar = total - money
    print(f"Less money ${bayar}")
else:
    print("Pass, Thank you!")
