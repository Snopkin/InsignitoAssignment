
from tkinter import messagebox

from microphone import Microphone
from src.acoustic_phased_array.main.acoustic_phased_array import AcousticArray
from src.acoustic_phased_array.main.simulator import Simulator
import tkinter as tk

class Main:
    def __init__(self, root_element):
        self.root = root_element
        self.root.title("Acoustic Array Simulator")

        # Microphone positions user input
        tk.Label(root_element, text="Microphone Positions (x1,y1 x2,y2 ...):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.mic_positions_entry = tk.Entry(root_element, width=50)
        self.mic_positions_entry.grid(row=0, column=1, padx=10, pady=5)

        # Frequency user input
        tk.Label(root_element, text="Frequency (Hz):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.frequency_entry = tk.Entry(root_element)
        self.frequency_entry.grid(row=1, column=1, padx=10, pady=5)

        # Look direction input
        tk.Label(root_element, text="Look Direction (degrees):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.initial_looking_direction_entry = tk.Entry(root_element)
        self.initial_looking_direction_entry.grid(row=2, column=1, padx=10, pady=5)

        # Angle resolution input
        tk.Label(root_element, text="Angle Resolution (degrees):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.angle_resolution_entry = tk.Entry(root_element)
        self.angle_resolution_entry.grid(row=3, column=1, padx=10, pady=5)

        # Start Simulation button
        self.start_button = tk.Button(root_element, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=4, columnspan=2, pady=20)

    def start_simulation(self):
        # Get input values
        mic_positions_str = self.mic_positions_entry.get()
        frequency_str = self.frequency_entry.get()
        initial_looking_direction_str = self.initial_looking_direction_entry.get()
        angle_resolution_str = self.angle_resolution_entry.get()

        try:
            mic_positions = [tuple(map(float, pos.split(','))) for pos in mic_positions_str.split()]
            frequency = float(frequency_str)
            initial_looking_direction = float(initial_looking_direction_str)
            angle_resolution = float(angle_resolution_str)
            if not mic_positions:
                raise ValueError("Microphone positions cannot be empty.")
            if frequency <= 0:
                raise ValueError("Frequency must be a positive number.")
            if not (0 <= initial_looking_direction < 360):
                raise ValueError("Look direction must be in the range [0, 360).")
            if angle_resolution <= 0:
                raise ValueError("Angle resolution must be a positive number.")

            if angle_resolution < 0.001:
                proceed = messagebox.askyesno(
                    "Warning",
                    "Angle resolution is very small, which may cause the simulation to be slow. Do you want to proceed?"
                )
                if not proceed:
                    return

            microphones = [Microphone(x, y) for x, y in mic_positions]
            acoustic_array = AcousticArray(microphones, frequency, initial_looking_direction, angle_resolution)
            radiation_pattern = acoustic_array.calculate_radiation_pattern()

            simulator = Simulator(acoustic_array)
            simulator.plot_radiation_pattern(radiation_pattern)


        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()