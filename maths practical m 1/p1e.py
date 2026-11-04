a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

print("Common Divisor are:")
for i in range(1, min(abs(a), abs(b)) + 1):
    if a % i == 0 and b % 1 == 0:
        print(i, end= " ")
