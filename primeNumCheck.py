def checkNumber(num):
    if num == 1 or num == 2:
        print(f"{num} Is a Prime Number\n")
    else:
        global x
        for x in range(2, num):
            if num%x==0:
                stat = 0
                break
            else:
                stat = 1
        checkStatus(stat)

def checkStatus(stat):
    if stat == 0:
        print(f"{num} Not a Prime Number")
        print(f"{x} kali {num//x} = {num}\n")
    else:
        print(f"{num} Is a Prime Number \n")

while True:
    num = int(input("Input Number : "))
    checkNumber(num)