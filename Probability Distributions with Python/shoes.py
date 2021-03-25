"""
Plot Probability Distribution for Women's Shoe Sizes
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_ROLLS = 1000

sample = np.random.normal(loc=5, scale=1, size=NUM_ROLLS)
sample = np.round(sample).astype(int)  # Convert to integers

# Numpy arrays containing counts for each side
side, count = np.unique(sample, return_counts=True)
probs = count / len(sample)

# Plot the results
sns.barplot(side, probs)
plt.title(
    f"Probability Distribution Women's Shoe Sizes ({NUM_ROLLS} rolls)")
plt.ylabel("Probability")
plt.xlabel("Outcome")
plt.show()
