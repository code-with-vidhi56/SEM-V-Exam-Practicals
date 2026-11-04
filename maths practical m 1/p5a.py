import matplotlib.pyplot as plt

 #Enter real and  imaginary part
x = float(input("enter real part:"))
y = float(input("enter imaginary part:"))

#plot the complex number
plt.axhline(0)
plt.axvline(0)

plt.scatter(x, y)
plt.plot([0, x], [0, y], linestyle = '--')

plt.xlabel("real Axis")
plt.ylabel("imaginary Axis")
plt.title("Complex Number on Argand plane")
plt.grid()
plt.show()
