import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(1000)
plt.scatter(range(1000), data, alpha=0.6, s=15)
plt.title("scatter plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
