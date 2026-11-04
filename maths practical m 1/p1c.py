#c=18, 54=972
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = abs(x)

if a == 0 or b==0:
    lcm = 0
else:
    lcm = abs(a*b)
print("Lcm= ",lcm)

