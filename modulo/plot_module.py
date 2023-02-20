import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()

    def plot_with_errorbars(self, errors):
        plt.errorbar(self.x, self.y, yerr=errors)
        plt.show()