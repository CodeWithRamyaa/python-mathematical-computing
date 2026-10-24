import numpy as np

A = np.array([[1, 2],
              [3, 4]], dtype=float)

n = len(A)
aug = np.hstack((A, np.eye(n)))

for i in range(n):
    # Find the best pivot row
    max_row = i + np.argmax(np.abs(aug[i:, i]))

    # Swap rows
    aug[[i, max_row]] = aug[[max_row, i]]

    # Check if inverse exists
    if abs(aug[i, i]) < 1e-10:
        print("Inverse does not exist.")
        break

    # Make the pivot equal to 1
    aug[i] = aug[i] / aug[i, i]

    # Make other elements in the column zero
    for j in range(n):
        if i != j:
            aug[j] = aug[j] - aug[j, i] * aug[i]

else:
    inverse = aug[:, n:]
    print("Inverse Matrix:")
    print(np.round(inverse, 2))
