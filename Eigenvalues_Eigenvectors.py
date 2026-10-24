import numpy as np

A = np.array([2, 3, 4])
B = np.array([3, -2, 0])

dot_product = np.dot(A, B)

print("Dot Product:", dot_product)

if dot_product == 0:
    print("The vectors are orthogonal.")
else:
    print("The vectors are not orthogonal.")
