import numpy as np
import matplotlib.pyplot as plt
class Simulator:
    def __init__(self, acoustic_array):
        self.acoustic_array = acoustic_array

    def plot_radiation_pattern(self, radiation_pattern):
        theta = np.radians(list(radiation_pattern.keys()))
        r = list(radiation_pattern.values())

        plt.figure(figsize=(8, 8))
        ax = plt.subplot(111, polar=True)
        ax.plot(theta, r)
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        plt.show()