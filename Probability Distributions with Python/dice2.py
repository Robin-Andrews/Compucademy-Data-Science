"""
Plot Discrete Probability Distribution for Biased 6-Sided Die
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_ROLLS = 1000

values = [1, 2, 3, 4, 5, 6]
probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

# Draw a weighted sample
sample = np.random.choice(values, NUM_ROLLS, p=probs)

# Numpy arrays containing counts for each side
side, count = np.unique(sample, return_counts=True)
probs = count / len(sample)

# Plot the results
sns.barplot(side, probs)
plt.title(
    f"Discrete Probability Distribution for Biased 6-Sided Die ({NUM_ROLLS} rolls)")
plt.ylabel("Probability")
plt.xlabel("Outcome")
plt.show()
