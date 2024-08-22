import math


class Microphone:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

    '''
    Calculates the phase shift of this microphone, relative to the referenced mocrophone,
    Assuming it's placed at the origin
    :param angle: The angle in rad between the direction of the incoming wave and the microphone.
    :type angle: float
    :param wave_frequency: The frequency of the sound wave in Hz.
    :type wave_frequency: float
    :param medium_speed: The speed of sound in the medium in m/s units, with a default value of 343.0 m/s.
    :type medium_speed: float
    :return: The phase shift of the microphone [radians].
    :rtype: float
    '''
    def calculate_phase_shift(self, initial_looking_direction_rad, frequency, wave_speed_in_medium=343.0):
        delta_r = self.x_coordinate * math.cos(initial_looking_direction_rad) + self.y_coordinate * math.sin(initial_looking_direction_rad)
        delta_t = delta_r / wave_speed_in_medium
        phase_shift = 2 * math.pi * frequency * delta_t
        return phase_shift

    '''
    returns a tuple of (x_position, y_position)
    '''
    def get_position(self):
        return self.x_coordinate,self.y_coordinate

