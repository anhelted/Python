print("This program will determine the number of days of a given month")
def dateMonth(month):
        if month in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if month == 2:
                year = int(input("Enter the year : "))
                dateYear(year)
            else:
                if month in [1,3,5,7,8,10,12]:
                    print("The are 31 days in the month")
                else:
                    print("The are 30 days in the month")
        else:
            print(f"Invalid value entered : {month}")

def dateYear(year):
        if year%4==0:
            print("The are 29 days in the month")
        else:
            print("The are 28 days in the month")

loop = True
while loop == True:
    print("Enter -1 to stop the program")
    month = int(input("Enter the month (1-12) : "))
    if month == -1:
        loop = False
        print("Thanks for using my program, see you again.")
    else:
        dateMonth(month)
