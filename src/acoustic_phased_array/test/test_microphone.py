import unittest

from src.acoustic_phased_array.main.microphone import Microphone


class TestMicrophone(unittest.TestCase):
    def test_calculate_phase_shift(self):
        mic = Microphone(0.1, 0.2)
        phase_shift = mic.calculate_phase_shift(initial_looking_direction_rad=0, wave_speed_in_medium=343, frequency=1000)
        expected_shift = 2 * 3.14159 * 1000 * (0.1 / 343)
        self.assertAlmostEqual(phase_shift, expected_shift, places=5)