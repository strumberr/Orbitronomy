import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from datetime import date
import csv


class datasetOrbit:
    def __init__(self, plot_title, name):

        self.name = name

        self.writer = PillowWriter(fps=30)

        self.plot_title = plot_title

        self.plt = plt

        self.fig = self.plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.object_dots = {}
        self.object_positions = {}
        self.orbital_periods = {}

        self.ax = self.fig.add_subplot(111, projection='3d')


    def datasetPlotStyle(self, background_color):

        self.plt.style.use(background_color)

        self.ax.set_facecolor(self.face_color)
        self.fig.patch.set_facecolor(self.face_color)

        self.ax.xaxis.set_pane_color(self.pane_color)
        self.ax.yaxis.set_pane_color(self.pane_color)
        self.ax.zaxis.set_pane_color(self.pane_color)

        self.ax.xaxis._axinfo["grid"]['color'] =  self.grid_color
        self.ax.yaxis._axinfo["grid"]['color'] =  self.grid_color
        self.ax.zaxis._axinfo["grid"]['color'] =  self.grid_color

        #text and label color
        self.ax.xaxis.label.set_color(self.label_color)
        self.ax.yaxis.label.set_color(self.label_color)
        self.ax.zaxis.label.set_color(self.label_color)

        self.ax.tick_params(axis='x', colors=self.tick_color)
        self.ax.tick_params(axis='y', colors=self.tick_color)
        self.ax.tick_params(axis='z', colors=self.tick_color)
        

        self.alpha = self.orbit_transparency
    
    def datasetCalculateOrbit(self, plot_steps, n_orbits, data=None, 
                        color=None, trajectory=False, sun=True, random_color=False,

                        delimiter=","
                        ):
        


        if sun:
            self.ax.scatter([0], [0], [0], color="yellow", s=100, label="Sun")
        else:
            pass

        
        if self.file_name:

            with open(self.file_name, mode='r') as file:
                csv_reader = csv.DictReader(file, delimiter=delimiter)
                

                for row in csv_reader:
                    self.steps = plot_steps
                    
                    self.object_id = row[self.column_name]
                    self.semi_major_axis = row[self.column_semi_major_axis]
                    self.perihelion = row[self.column_perihelion]
                    self.eccentricity = row[self.column_eccentricity]

                    if self.eccentricity == 1:
                        self.eccentricity = 1.0000000000000001e-10

                    self.inclination = row[self.column_inclination]
                    self.longitude_of_ascending_node = row[self.column_longitude_of_ascending_node]
                    self.argument_of_perihelion = row[self.column_argument_of_perihelion]


                    self.object_orbit = pyasl.KeplerEllipse(a=float(self.semi_major_axis), per=float(self.perihelion), e=float(self.eccentricity), Omega=float(self.longitude_of_ascending_node), i=float(self.inclination), w=float(self.argument_of_perihelion))

                    self.t_object = np.linspace(0, 4 * n_orbits, plot_steps)
                    self.pos_object = self.object_orbit.xyzPos(self.t_object)

                    if color == None:
                        if random_color:
                            r = lambda: np.random.randint(0,255)
                            self.color = '#%02X%02X%02X' % (r(),r(),r())
                        else:
                            try:
                                self.color = row[self.column_color]
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

                    self.object_dot = self.ax.scatter([self.pos_object[0][0]], [self.pos_object[0][1]], [self.pos_object[0][2]], color=self.color, label=f"{self.object_id}")

                    if trajectory:
                        self.ax.plot(self.pos_object[:,0], self.pos_object[:,1], self.pos_object[:,2], color=self.color, alpha=self.alpha, linewidth=1)
                    else:
                        pass

                    self.object_dots[self.object_id] = self.object_dot

                    a = float(self.semi_major_axis)
                    orbital_period = np.sqrt(a**3)
                    self.orbital_periods[self.object_id] = orbital_period

        else:
            raise ValueError("No file name given")






    def animate_before(self, i):

        self.min_period = max(self.orbital_periods.values())
        self.relative_speeds = {}

        for unit, period in self.orbital_periods.items():
            
            relative_speed = self.min_period / period

            self.relative_speeds[unit] = relative_speed

        self.vicinity_radius = 3


        for unit, object_dot in self.object_dots.items():
            pos_index = int(i) % len(self.object_positions[unit])
            pos_object = self.object_positions[unit][pos_index]

            object_dot._offsets3d = (np.array([pos_object[0]]), np.array([pos_object[1]]), np.array([pos_object[2]]))


        self.fig.canvas.draw()

        return list(self.object_dots.values())
    


    def datasetAnimateOrbit(self, dpi, save=False, export_zoom=None, 
                     font_size="xx-small", export_folder=None,
                     x_lim=None, y_lim=None, z_lim=None,
                     x_label="X-Axis", y_label="Y-Axis", z_label="Z-Axis"
                     ):


        self.vicinity_radius = export_zoom

        myAnimation = animation.FuncAnimation(self.fig, self.animate_before, interval=40, frames=np.arange(0, self.steps), blit=True, repeat=True)

        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_zlabel(z_label)

        self.plt.legend(loc="lower right", fontsize=font_size)
        self.plt.title(f'{self.name}')


        if x_lim:
            self.ax.set_xlim(-x_lim[0], x_lim[1])
        if y_lim:
            self.ax.set_ylim(-y_lim[0], y_lim[1])
        if z_lim:
            self.ax.set_zlim(-z_lim[0], z_lim[1])


        if save:

            if export_folder:
                myAnimation.save(f'{export_folder}/{self.name}-orbit.gif', writer=self.writer, dpi=dpi)
            else:
                myAnimation.save(f'{self.name}-orbit.gif', writer=self.writer, dpi=dpi)
            
            self.plt.show()

        else:

        
            self.plt.show()

    #limiting the plot
    def xLim(self, x_lim):
        self.ax.set_xlim(-x_lim[0], x_lim[1])

    def yLim(self, y_lim):
        self.ax.set_ylim(-y_lim[0], y_lim[1])
    
    def zLim(self, z_lim):
        self.ax.set_zlim(-z_lim[0], z_lim[1])


    #labeling the plot
    def xLabel(self, x_label):
        self.ax.set_xlabel(x_label)
    
    def yLabel(self, y_label):
        self.ax.set_ylabel(y_label)
    
    def zLabel(self, z_label):
        self.ax.set_zlabel(z_label)


    #columns for the dataset
    def columnSemiMajorAxis(self, column_semi_major_axis):
        self.column_semi_major_axis = column_semi_major_axis

    def columnPerihelion(self, column_perihelion):
        self.column_perihelion = column_perihelion

    def columnEccentricity(self, column_eccentricity):
        self.column_eccentricity = column_eccentricity

    def columnInclination(self, column_inclination):
        self.column_inclination = column_inclination

    def columnLongitudeOfAscendingNode(self, column_longitude_of_ascending_node):
        self.column_longitude_of_ascending_node = column_longitude_of_ascending_node

    def columnArgumentOfPerihelion(self, column_argument_of_perihelion):
        self.column_argument_of_perihelion = column_argument_of_perihelion

    def columnColor(self, column_color):
        self.column_color = column_color

    def columnName(self, column_name):
        self.column_name = column_name

    #filename
    def fileName(self, file_name):
        self.file_name = file_name

    #style
    def faceColor(self, face_color):
        self.face_color = face_color

    def paneColor(self, pane_color):
        self.pane_color = pane_color

    def gridColor(self, grid_color):
        self.grid_color = grid_color

    def orbitTransparency(self, orbit_transparency):
        self.orbit_transparency = orbit_transparency

    def labelColor(self, label_color):
        self.label_color = label_color

    def tickColor(self, tick_color):
        self.tick_color = tick_color
    

    


# test = datasetOrbit(plot_title="Test", name="Earth")


# #styling
# test.faceColor("black")
# test.paneColor("black")
# test.gridColor("#222831")
# test.orbitTransparency(0.5)
# test.labelColor("white")
# test.tickColor("white")


# test.datasetPlotStyle(background_color="dark_background")


# #name of the columns in the dataset in CSV format
# test.columnSemiMajorAxis("semi_major_axis")
# test.columnPerihelion("perihelion")
# test.columnEccentricity("eccentricity")
# test.columnInclination("inclination")
# test.columnLongitudeOfAscendingNode("longitude_of_ascending_node")
# test.columnArgumentOfPerihelion("argument_of_perihelion")
# test.columnColor("color")
# test.columnName("name")

# #name of the dataset file
# test.fileName("datasets/Planetary-Satellite-Data.csv")


# test.datasetCalculateOrbit(plot_steps=1000, n_orbits=12, color="yellow", 
#                     random_color=True, trajectory=True, sun=True,
#                     delimiter=";"
# )

#you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([0.1, 0.1])

# test.xLabel("X-Axis")
# test.yLabel("Y-Axis")
# test.zLabel("Z-Axis")

# test.datasetAnimateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small")

