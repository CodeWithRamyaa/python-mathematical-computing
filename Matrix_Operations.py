import numpy as np

A = np.array([[2, 1, 1],
              [1, 2, 1],
              [1, 1, 2]], dtype=float)

B = np.array([100, 120, 110], dtype=float)

X = np.linalg.solve(A, B)

print("Production quantities:")
print("Product A:", round(X[0], 2))
print("Product B:", round(X[1], 2))
print("Product C:", round(X[2], 2))
