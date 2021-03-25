"""
Algorithm for sampling from discrete probability distribution.
"""

import numpy as np

# Vector of probabilities
p = [0.1, 0.2, 0.3, 0.4]

# Uniform [0, 1)
u = np.random.rand()

# Here's the algorithm
i = 0
while u > 0:
    u -= p[i]
    i += 1

# The variable `i` now has the desired distribution
print(i)