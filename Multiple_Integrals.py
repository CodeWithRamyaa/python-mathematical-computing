import matplotlib.pyplot as plt

x = [1, 4, 4, 1, 1]
y = [1, 1, 3, 3, 1]

reflected_x = [-i for i in x]

plt.plot(x, y, marker='o', label="Original Polygon")
plt.plot(reflected_x, y, marker='o', label="Reflected Polygon")

plt.axhline(0)
plt.axvline(0)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Reflection of Polygon About Y-axis")
plt.legend()
plt.grid()
plt.show()
