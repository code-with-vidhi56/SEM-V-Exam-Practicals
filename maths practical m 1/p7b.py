import matplotlib.pyplot as plt
n =10

sequence = list(range(1, n+1))

print("Natural number Sequence:")
print(sequence)

plt.plot(range(1, n+1), sequence, marker='o')
plt.xlabel("n")
plt.ylabel("a(n)")
plt.title("Natural number Sequence")
plt.grid()
plt.show()
