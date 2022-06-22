cache = {}

def fibonacci(x):
    if x in cache:
        return cache[x]

    if x == 1:
        value = 1
    elif x == 2:
        value = 1
    elif x > 2 :
        value = fibonacci(x-1) + fibonacci(x-2)
    
    cache[x] = value
    return value

while True:
    print("Calculate fibonacci numbers using recursive function")
    num = int(input("Input Number : ")); fibonacci(num)
    print(f"Fibonacci num-{num} is {fibonacci(num)}\n")
