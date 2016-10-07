def fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b
        
lim = int(input("How many numbers? "))
print("\n")
count = 0
for num in fib():
    print(num)
    count += 1
    if count >= lim:
        break
