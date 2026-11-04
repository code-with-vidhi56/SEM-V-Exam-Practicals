import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

g = math.gcd(a, m)

if g !=1:
    print("GCD(a, m) =", g)
    print("Since GCD is not 1, modular inverse does not exist.")

else:
    inverse = pow(a, -1, m)
    x = (inverse *b )%m

    print("GCD(a, m) =", g)
    print("Multiplicative inverse of", a, "modulo", m, "=", inverse)
    print("Solution: x=", x)
