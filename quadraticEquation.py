from math import sqrt

print("--Program to Find Quadratic Equations--")
print("=====================================")
a = int(input("input coefficient A = "))
b = int(input("input coefficient B = "))
c = int(input("input coefficient C = "))

d = (b**2) - (4*a*c)

if a == 0:
    print("Coefficient A cannot be equal to 0")
else:
    print(f"Quadratic Equation {a} x^2 + {b}x + {c}")
    print(f"Determine = {d}")

    if d < 0:
        print("Root of Imaginer")
        print(f"Root x1 = -{b} + Root {d} / {b} * {a}")
        print(f"Root x2 = -{b} - Root {d} / {b} * {a}")
    elif d == 0:
        x1 = -b / (2*a)
        x2 = x1
        print("Twin Roots")
        print(f"Root x1 = {x1}")
        print(f"Root x2 = {x2}")
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print("Different Roots")
        print(f"Roots x1 = {x1}")
        print(f"Roots x2 = {x2}")
