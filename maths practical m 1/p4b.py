# 5,7,12=1,5,11
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



    #5x--- 7(mod 12) the invers of 5 modulo 12 is 5 because 5*5 =25--- 1(mod 12)
    #multiply both side by 5
    #x--- 5(7) (mod 12)
    #x---35 (mod 12)
    #5(11) = 55
    #55/12
    #therfore x---11(mod 12)
