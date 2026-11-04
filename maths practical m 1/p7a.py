import matplotlib.pyplot as plt

# First term and common differences
a = 2
d = 3
n =10

sequence = []
for i in range(n):
    term = a+i*d
    sequence.append(term)

print("Arithmetic Sequence:")
print(sequence)
#plot
plt.plot(range(1, n+1), sequence, marker='o')
plt.xlabel("n")
plt.ylabel("a(n)")
plt.title("Arithmetic sequence")
plt.grid()
plt.show()
