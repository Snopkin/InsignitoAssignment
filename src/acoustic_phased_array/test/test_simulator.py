import unittest

from src.acoustic_phased_array.main.acoustic_phased_array import AcousticArray
from src.acoustic_phased_array.main.microphone import Microphone
from src.acoustic_phased_array.main.simulator import Simulator


class TestSimulator(unittest.TestCase):
    def test_plot_radiation_pattern(self):
        microphones = [Microphone(0, 0), Microphone(0.1, 0)]
        acoustic_array = AcousticArray(microphones, 1000, 90, 1)
        radiation_pattern = acoustic_array.calculate_radiation_pattern()
        simulator = Simulator(acoustic_array)
        try:
            simulator.plot_radiation_pattern(radiation_pattern)
        except Exception as e:
            self.fail(f"Simulator.plot_radiation_pattern() raised {type(e).__name__} unexpectedly!")
