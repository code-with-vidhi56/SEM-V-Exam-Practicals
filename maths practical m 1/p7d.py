import matplotlib.pyplot as plt

n =10

sequence = [i ** 2 for i in range(1, n+1)]

print(" Sequence:")
print(sequence)

plt.bar(range(1, n+1), sequence)
plt.xlabel("n")
plt.ylabel("n^2")
plt.title("Square Sequence  ")
plt.show()
