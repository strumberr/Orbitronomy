import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from datetime import date
import math


class FeaturesExtra():
    
    def __init__(self, ax, alpha=1):
        self.ax = ax

        self.inclination_plot_color = "white"
        self.inclination_plot = False


    def inclinationObserver(self, semi_major_axis,
                        perihelion, eccentricity, 
                        longitude_of_ascending_node, 
                        inclination, argument_of_perihelion, 
                        actual_orbit, n_orbits, plot_steps):

        # Orbit with inclination set to 0 (projection)
        projected_orbit = pyasl.KeplerEllipse(a=float(semi_major_axis), per=float(perihelion), 
                                            e=float(eccentricity), Omega=float(longitude_of_ascending_node), 
                                            i=float(0), w=float(argument_of_perihelion))

        # Generate positions for the actual orbit and the projection
        t_values = np.linspace(0, 4 * n_orbits, plot_steps)
        actual_positions = actual_orbit.xyzPos(t_values)
        projected_positions = projected_orbit.xyzPos(t_values)

        # Plot the projected orbit
        self.ax.plot(projected_positions[:,0], projected_positions[:,1], projected_positions[:,2], 
                    color=self.inclination_plot_color, alpha=self.alpha, linewidth=1)

        # Draw a line at every step of the orbit
        for i in range(0, len(actual_positions), 6):
            actual_pos = actual_positions[i]
            projected_pos = projected_positions[i]

            # Draw line between actual position and projected position
            self.ax.plot([actual_pos[0], projected_pos[0]], 
                        [actual_pos[1], projected_pos[1]], 
                        [actual_pos[2], projected_pos[2]], 
                        color=self.inclination_plot_color, alpha=self.alpha, linewidth=1)

        # Convert inclination to degrees for display
        inclination_degrees = inclination

        # Choose a point on the actual orbit to display the inclination text (e.g., the first point)
        actual_pos = actual_positions[len(actual_positions)//2]  # Place the text halfway through the orbit trajectory

        semi_major_axis = math.ceil(float(semi_major_axis))
        z_offset = semi_major_axis * 0.5  # Height of the vertical line above the actual position
        self.ax.plot([actual_pos[0], actual_pos[0]], 
                    [actual_pos[1], actual_pos[1]], 
                    [actual_pos[2], actual_pos[2] + z_offset], 
                    color=self.inclination_plot_color, alpha=self.alpha, linestyle='--', linewidth=1)

        # Display the inclination in degrees at the top of the vertical line
        text_position = (actual_pos[0], actual_pos[1], actual_pos[2] + z_offset)
        self.ax.text(text_position[0], text_position[1], text_position[2], 
                    f'{float(inclination_degrees):.2f}°', 
                    color=self.inclination_plot_color, fontsize=10, weight='semibold')
        

        # Set aspect ratio
        self.ax.set_aspect('equal')

        
        
        
    def display_name(self, current_pos, object_id, color, fontsize, fontweight):
        self.ax.text(current_pos[0], current_pos[1], current_pos[2], object_id, color=color, fontsize=fontsize, weight=fontweight)