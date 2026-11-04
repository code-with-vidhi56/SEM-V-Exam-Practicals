#48,18 =6
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

while b!= 0:
    remainder = a%b
    a=b
    b=remainder
print("GCD= ", abs(a))
