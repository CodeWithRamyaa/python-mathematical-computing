import numpy as np

A = np.array([1, 0, 0])
B = np.array([1, 1, 0])

dot_product = np.dot(A, B)

magnitude_A = np.linalg.norm(A)
magnitude_B = np.linalg.norm(B)

cos_theta = dot_product / (magnitude_A * magnitude_B)

angle = np.degrees(np.arccos(cos_theta))

print("Angle between the vectors:", round(angle, 2), "degrees")
