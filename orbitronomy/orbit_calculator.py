import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from datetime import date

class OrbitalProcessor:
    def __init__(self):
        self.column_name = None
        self.column_semi_major_axis = None
        self.column_perihelion = None
        self.column_eccentricity = None
        self.column_inclination = None
        self.column_longitude_of_ascending_node = None
        self.column_argument_of_perihelion=None
        self.column_color = None


    def orbitMathProcessingDataset(self, row, column_name, column_semi_major_axis, 
                                   column_perihelion, column_eccentricity, 
                                   column_inclination, column_longitude_of_ascending_node, 
                                   column_argument_of_perihelion, 
                                   column_color, color, random_color, n_orbits, plot_steps, trajectory, 
                                   sun, planet_size, alpha, ax, object_positions, 
                                   object_dots, orbital_periods):
        
        self.object_id = row[column_name]
        self.semi_major_axis = row[column_semi_major_axis]
        self.perihelion = row[column_perihelion]
        self.eccentricity = row[column_eccentricity]

        if self.eccentricity == 1:
            self.eccentricity = 1.0000000000000001e-10

        self.inclination = row[column_inclination]
        self.longitude_of_ascending_node = row[column_longitude_of_ascending_node]
        self.argument_of_perihelion = row[column_argument_of_perihelion]


        self.object_orbit = pyasl.KeplerEllipse(a=float(self.semi_major_axis), per=float(self.perihelion), e=float(self.eccentricity), Omega=float(self.longitude_of_ascending_node), i=float(self.inclination), w=float(self.argument_of_perihelion))

        self.t_object = np.linspace(0, 4 * n_orbits, plot_steps)
        self.pos_object = self.object_orbit.xyzPos(self.t_object)

        if color == None:
            if random_color:
                r = lambda: np.random.randint(0,255)
                self.color = '#%02X%02X%02X' % (r(),r(),r())
            else:
                try:
                    self.color = row[column_color]
                except:
                    r = lambda: np.random.randint(0,255)
                    self.color = '#%02X%02X%02X' % (r(),r(),r())
            
        else:
            if random_color:
                r = lambda: np.random.randint(0,255)
                self.color = '#%02X%02X%02X' % (r(),r(),r())
            else:
                self.color = color

        self.ax.set_aspect('equal')

        

        self.object_positions[self.object_id] = self.pos_object

        self.object_dot = self.ax.scatter([self.pos_object[0][0]], [self.pos_object[0][1]], [self.pos_object[0][2]], color=self.color, label=f"{self.object_id}", s=self.planet_size)

        if trajectory:
            self.ax.plot(self.pos_object[:,0], self.pos_object[:,1], self.pos_object[:,2], color=self.color, alpha=self.alpha, linewidth=1)
        else:
            pass

        self.object_dots[self.object_id] = self.object_dot

        a = float(self.semi_major_axis)
        orbital_period = np.sqrt(a**3)
        self.orbital_periods[self.object_id] = orbital_period

        