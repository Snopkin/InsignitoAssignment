import unittest

from src.acoustic_phased_array.main.acoustic_phased_array import AcousticArray
from src.acoustic_phased_array.main.microphone import Microphone


class TestAcousticArray(unittest.TestCase):
    def setUp(self):
        self.microphones = [Microphone(0, 0), Microphone(0.1, 0)]
        self.frequency = 1000
        self.look_direction = 90
        self.angle_resolution = 1
        self.acoustic_array = AcousticArray(self.microphones, self.frequency, self.look_direction, self.angle_resolution)

    def test_initial_phase_shifts(self):
        phase_shifts = self.acoustic_array._calculate_initial_phase_shifts()
        self.assertEqual(len(phase_shifts), 2)
        self.assertNotEqual(phase_shifts[0], phase_shifts[1])

    def test_calculate_gain(self):
        gain = self.acoustic_array.calculate_gain(90)
        self.assertGreater(gain, 0)

    def test_calculate_radiation_pattern(self):
        pattern = self.acoustic_array.calculate_radiation_pattern()
        self.assertEqual(len(pattern), 360)
        self.assertIn(90, pattern)
        self.assertGreater(pattern[90], 0)