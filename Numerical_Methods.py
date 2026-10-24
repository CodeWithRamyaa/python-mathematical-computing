import numpy as np

x = 1
y = 2

# Function: f(x, y) = x^2 + y^2

df_dx = 2 * x
df_dy = 2 * y

gradient = np.array([df_dx, df_dy])

direction = np.array([3, 4])
unit_direction = direction / np.linalg.norm(direction)

derivative = np.dot(gradient, unit_direction)

print("Gradient:", gradient)
print("Directional Derivative:", round(derivative, 2))
