#3,4= 5.00cos53.13+isin53.13
import cmath
import math

#input complex number
x = float(input("enter real part:"))
y = float(input("enter imaginary part:"))
z = complex(x, y)

#convert to polar form
r, theta = cmath.polar(z)

#convert angles from radians to degrees
theta_degree = math.degrees(theta)

print("\n Complex numbers =" , z)
print("Modulus (r) =", r)
print("Argument (theta) in radians =", theta)
print("Argument (theta) in degrees =", theta_degree )

print("\nPolar form:")
print(f"{r:.2f} (cos({theta_degree:.2f} ) + i sin({theta_degree:.2f}  ))")
