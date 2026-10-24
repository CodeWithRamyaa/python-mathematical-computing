import numpy as np

A = np.array([[2, 1],
              [1, 3]])

v = np.array([2, 4])

image = np.dot(A, v)

print("Original Vector:")
print(v)

print("Image of the Vector:")
print(image)
