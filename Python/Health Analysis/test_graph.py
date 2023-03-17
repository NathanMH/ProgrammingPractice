import matplotlib.pyplot as plt
import numpy as np


def plotnormal():
    return plt.plot(np.random.randn(1000), np.random.randn(1000), "o", alpha=0.3)


plotnormal()
plt.show()
