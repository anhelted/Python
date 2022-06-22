#convert decimal to hexa
def decToHex(decimal):
    decimal, hexa = decimal // 16, HEXA[decimal % 16]
    if decimal:
        return decToHex(decimal) + hexa
    return hexa

print("convert decimal to hexa")
HEXA = "0123456789ABCDEF"
decimal = int(input("Decimal     : "))
print(f"Hexadecimal : 0x{decToHex(decimal)}\n")

#convert hexa to decimal
def hexToDec(hexa):
    return int(hexa, 16)

print("convert hexa to decimal")
hexa = str(input("Hexadecimal : "))
print(f"Decimal     : {hexToDec(hexa)}")
