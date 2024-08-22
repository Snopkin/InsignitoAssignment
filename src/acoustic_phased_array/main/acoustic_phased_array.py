import math
import numpy as np
import matplotlib.pyplot as plt


class AcousticArray:
    def __init__(self, microphones, frequency, initial_looking_direction, angle_resolution):
        self.microphones = microphones
        self.frequency = frequency
        self.initial_looking_direction = initial_looking_direction
        self.angle_resolution = angle_resolution
        self.sound_speed = 343 #todo get from user?
        self.initial_looking_direction_rad = math.radians(initial_looking_direction)
        self.initial_phase_shifts = self._calculate_initial_phase_shifts()

    '''
    computes initial phase shifts for each microphone to align the array with the specified look direction.
    '''
    def _calculate_initial_phase_shifts(self):
        phase_shifts = [
            mic.calculate_phase_shift(self.initial_looking_direction_rad, self.sound_speed, self.frequency)
            for mic in self.microphones
        ]
        return phase_shifts

    '''
    calculates the signal strength for a specified azimuth by summing and squaring phase-aligned signals from all microphones.
    '''
    #TODO: maybe should be gain? (signal ** 2)
    def calculate_gain(self, azimuth):
        azimuth_rad = math.radians(azimuth)
        total_signal = 0
        for mic, initial_phase_shift in zip(self.microphones, self.initial_phase_shifts):
            delta_r = mic.x_coordinate * math.cos(azimuth_rad) + mic.y_coordinate * math.sin(azimuth_rad)
            delta_t = delta_r / self.sound_speed
            signal_phase = 2 * math.pi * self.frequency * delta_t - initial_phase_shift
            signal = math.cos(signal_phase)
            total_signal += signal
        return abs(total_signal)

    def calculate_radiation_pattern(self):
        azimuths = np.arange(0, 360, self.angle_resolution)
        radiation_pattern = {
            azimuth: self.calculate_gain(azimuth)
            for azimuth in azimuths
        }
        return radiation_pattern