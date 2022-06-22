title = str(input("Input Title : "))
filename = (f"{title}.txt")
f = open(filename, "w")
print(f"File {filename} successfully made!")
print('----------------------------------')
print("Type \"N\" to end poetry")

rows = True
while rows == True:
    poetry = str(input(""))
    if poetry == "N" or poetry == "n":
        print("----------------------------------")
        print("Successfully! Here is the content of the poem you made")
        print("----------------------------------")
        rows = False
    else:
        f.write(poetry)
        f.write('\n')

f = open(f"{title}.txt", "r")
print(f.read())
