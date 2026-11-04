#1,1,4 = -4+0j
import cmath
import math

#Enter  real and  imaginary part
a= float(input("enter real part:"))
b = float(input("enter imaginary part:"))

#enter power
n = int(input("Enter power n:"))
#Create Complex number
z = complex(a, b)
#convert to polar form
r = abs(z)
theta = cmath.phase(z)

#apply De Moivre's theorem
result = (r ** n) * (
    math.cos(n * theta) + 1j * math.sin(n*theta)
)

print("\n Complex numbers =" , z)
print("Modulus (r) =", r)
print("Argument theta =", math.degrees(theta), "degrees")

print("\nUsing De Moivre theorem:")
print("z^n =", result)
#Direct calculation for varification
print("Direct Python calculation :")
print("z^n=" , z ** n)







