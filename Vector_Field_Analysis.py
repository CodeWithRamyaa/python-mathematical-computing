import numpy as np

# Define the vector field F = (P, Q, R)
def P(x, y, z):
    return x**2

def Q(x, y, z):
    return y**2

def R(x, y, z):
    return z**2

# Define the point
x, y, z = 1.0, 2.0, 3.0

# Small step for numerical differentiation
h = 1e-5

# Calculate partial derivatives
dP_dx = (P(x+h, y, z) - P(x-h, y, z)) / (2*h)
dP_dy = (P(x, y+h, z) - P(x, y-h, z)) / (2*h)
dP_dz = (P(x, y, z+h) - P(x, y, z-h)) / (2*h)

dQ_dx = (Q(x+h, y, z) - Q(x-h, y, z)) / (2*h)
dQ_dy = (Q(x, y+h, z) - Q(x, y-h, z)) / (2*h)
dQ_dz = (Q(x, y, z+h) - Q(x, y, z-h)) / (2*h)

dR_dx = (R(x+h, y, z) - R(x-h, y, z)) / (2*h)
dR_dy = (R(x, y+h, z) - R(x, y-h, z)) / (2*h)
dR_dz = (R(x, y, z+h) - R(x, y, z-h)) / (2*h)

# Calculate divergence
divergence = dP_dx + dQ_dy + dR_dz

# Calculate curl
curl_x = dR_dy - dQ_dz
curl_y = dP_dz - dR_dx
curl_z = dQ_dx - dP_dy

# Display the results
print("Divergence:", round(divergence, 2))
print("Curl:", (round(curl_x, 2),
               round(curl_y, 2),
               round(curl_z, 2)))
