# import tkinter as tk
# from tkinter import messagebox
# import numpy as np
#
# class MainClass:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Ray Tracing Simulation")
#
#         # Create a frame to hold the label and entry for number of rays
#         self.rays_frame = tk.Frame(root)
#         self.rays_frame.pack(pady=10)
#
#         # Label and entry for the number of rays
#         self.rays_label = tk.Label(self.rays_frame, text="Number of Rays:")
#         self.rays_label.pack(side="left", padx=5)
#         self.rays_entry = tk.Entry(self.rays_frame)
#         self.rays_entry.pack(side="left", padx=5)
#
#         # Create a frame to hold the label and entry for y boundary
#         self.y_boundary_frame = tk.Frame(root)
#         self.y_boundary_frame.pack(pady=10)
#
#         # Label and entry for the y boundary
#         self.y_boundary_label = tk.Label(self.y_boundary_frame, text="y boundary:")
#         self.y_boundary_label.pack(side="left", padx=5)
#         self.y_boundary_entry = tk.Entry(self.y_boundary_frame)
#         self.y_boundary_entry.pack(side="left", padx=5)
#
#         # Create and pack the button below the input frames
#         self.button = tk.Button(root, text="Start Simulation", command=self.run)
#         self.button.pack(pady=20)
#
#     def run(self):
#         try:
#             # Get the number of rays from the entry widget
#             number_of_rays = int(self.rays_entry.get())
#             y_boundary = int(self.y_boundary_entry.get())
#             if not 1 <= number_of_rays <= 50:
#                 raise ValueError("Number of rays must be between 1 and 50.")
#
#             self.root.destroy()
#             # Here you would run the simulation
#             sim = Simulator(number_of_rays=number_of_rays, max_iterations=1000, y_boundary= y_boundary )
#             sim.simulate()
#             sim.plot_paths()
#
#
#         except ValueError as e:
#             # Show an error message if the input is invalid
#             messagebox.showerror("Input Error", str(e))
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     main_instance = MainClass(root)
#     root.mainloop()

from microphone import Microphone
from src.acoustic_phased_array.acoustic_phased_array import AcousticArray
from src.acoustic_phased_array.simulator import Simulator


class Main:
    @staticmethod
    def run():
        microphone_positions = [(0, 0), (0.1, 0), (0.2, 0)]  # Example positions in meters
        frequency = 1000  # Example frequency in Hz
        look_direction = 90  # Example look direction in degrees
        angle_resolution = 0.5  # Example resolution in degrees

        microphones = [Microphone(x, y) for x, y in microphone_positions]

        acoustic_array = AcousticArray(microphones, frequency, look_direction, angle_resolution)

        radiation_pattern = acoustic_array.calculate_radiation_pattern()

        # OUTPUT
        print(radiation_pattern)

        simulator = Simulator(acoustic_array)
        simulator.plot_radiation_pattern(radiation_pattern)

# Run the program
if __name__ == "__main__":
    Main.run()