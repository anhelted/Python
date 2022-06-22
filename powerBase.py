print("This is a negative and positive power program")

def powerBasis(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / (base * powerBasis(base, abs(power)-1))
    else:
        return base * powerBasis(base, power-1)

while True:
    base = int(input("Input Number : "))
    power = int(input("Input Number : "))
    print(powerBasis(base, power),"\n")
