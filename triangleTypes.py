a = int(input("input side A : "))
b = int(input("input side B : "))
c = int(input("input side C : "))

if a+b<=c or b+c<=a or c+a<=b:
    print("Not a Triangle")
elif a == b and b == c :
    print("Equilateral Triangle")
elif a == b or a == c or b == c :
    print("Isosceles Triangle")
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a :
    print("Right Triangle")
else :
    print("Scalene Triangle")
