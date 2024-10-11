import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from datetime import date
import csv
from ..ingredientes.features import *


class SimpleOrbit(FeaturesExtra):
    def __init__(self, plot_title, name, fps=30):
        
        self.name = name

        self.writer = PillowWriter(fps=fps)

        self.plot_title = plot_title

        self.plt = plt

        self.fig = self.plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.object_dots = {}
        self.object_positions = {}
        self.orbital_periods = {}

        self.ax = self.fig.add_subplot(111, projection='3d')

        super().__init__(self.ax)

        self.sun_size = 100

        self.face_color = "white"
        self.pane_color = "white"
        self.grid_color = "black"
        self.orbit_transparency = 0.5
        self.label_color = "black"
        self.tick_color = "black"

        self.planet_size = 100
        










    def plotStyle(self, background_color):

        self.plt.style.use(background_color)

        self.ax.set_facecolor(self.face_color)
        self.fig.patch.set_facecolor(self.face_color)

        self.ax.xaxis.set_pane_color(self.pane_color)
        self.ax.yaxis.set_pane_color(self.pane_color)
        self.ax.zaxis.set_pane_color(self.pane_color)

        self.ax.xaxis._axinfo["grid"]['color'] = self.grid_color
        self.ax.yaxis._axinfo["grid"]['color'] = self.grid_color
        self.ax.zaxis._axinfo["grid"]['color'] = self.grid_color

        #text and label color
        self.ax.xaxis.label.set_color(self.label_color)
        self.ax.yaxis.label.set_color(self.label_color)
        self.ax.zaxis.label.set_color(self.label_color)

        self.ax.tick_params(axis='x', colors=self.tick_color)
        self.ax.tick_params(axis='y', colors=self.tick_color)
        self.ax.tick_params(axis='z', colors=self.tick_color)
        

        self.alpha = self.orbit_transparency

    
    def calculateOrbit(self, plot_steps, n_orbits, data=None, 
                       color=None, trajectory=False, 
                       sun=True, inclinationObserver=False, 
                       display_name=False,
                       fontsize=12, fontweight="semibold", fontcolor="black"):
        
        self.inclination_plot = inclinationObserver
        
        if data:

            if sun:
                self.ax.scatter([0], [0], [0], color="yellow", s=self.sun_size, label="Sun")
            else:
                pass
            
            for el in data:

                self.steps = plot_steps
                self.object_id = el[0]
                self.semi_major_axis = el[1]
                self.perihelion = el[2]
                self.eccentricity = el[3]

                if self.eccentricity == 1:
                    self.eccentricity = 1.0000000000000001e-10

                self.inclination = el[4]
                self.longitude_of_ascending_node = el[5]
                self.argument_of_perihelion = el[6]


            
                self.object_orbit = pyasl.KeplerEllipse(a=float(self.semi_major_axis), per=float(self.perihelion), e=float(self.eccentricity), Omega=float(self.longitude_of_ascending_node), i=float(self.inclination), w=float(self.argument_of_perihelion))

                
                
                if self.inclination_plot:
                    self.inclinationObserver(self.semi_major_axis, self.perihelion, 
                                                self.eccentricity, self.longitude_of_ascending_node, 
                                                self.inclination, self.argument_of_perihelion, 
                                                self.object_orbit, n_orbits, plot_steps)
                else:
                    pass

                self.t_object = np.linspace(0, 4 * n_orbits, plot_steps)
                self.pos_object = self.object_orbit.xyzPos(self.t_object)

                if color == None:
                    try:
                        self.color = el[7]
                    except:
                        r = lambda: np.random.randint(0,255)
                        self.color = '#%02X%02X%02X' % (r(),r(),r())
                    
                else:
                    try:
                        self.color = el[7]
                    except:
                        self.color = color

                self.ax.set_aspect('equal')

                if display_name:
                    current_pos = self.pos_object[0]
                    self.display_name(current_pos, self.object_id, self.color, fontsize=fontsize, fontweight=fontweight)
                
                    
                self.object_positions[self.object_id] = self.pos_object

                self.object_dot = self.ax.scatter([self.pos_object[0][0]], [self.pos_object[0][1]], [self.pos_object[0][2]], color=self.color, label=f"{self.object_id}", s=self.planet_size)


                # #--------------------------------------------

                # #draw line between sun and object
                # lineDrawn = self.drawLine.drawLineTwoPoints([0, 0, 0], [self.pos_object[0][0], self.pos_object[0][1], self.pos_object[0][2]])

                # self.ax.plot(lineDrawn[0], lineDrawn[1], lineDrawn[2], color=self.color, alpha=self.alpha, linewidth=1)
                
                # #--------------------------------------------


                if trajectory:
                    self.ax.plot(self.pos_object[:,0], self.pos_object[:,1], self.pos_object[:,2], color=self.color, alpha=self.alpha, linewidth=1)
                else:
                    pass

                self.object_dots[self.object_id] = self.object_dot

        else:

            self.steps = plot_steps
            self.semi_major_axis = self.semi_major_axis
            self.perihelion = self.perihelion
            self.eccentricity = self.eccentricity

            if self.eccentricity == 1:
                self.eccentricity = 1.0000000000000001e-10

            self.inclination = self.inclination
            self.longitude_of_ascending_node = self.longitude_of_ascending_node
            self.argument_of_perihelion = self.argument_of_perihelion

            self.object_orbit = pyasl.KeplerEllipse(a=float(self.semi_major_axis), per=float(self.perihelion), e=float(self.eccentricity), Omega=float(self.longitude_of_ascending_node), i=float(self.inclination), w=float(self.argument_of_perihelion))

            self.t_object = np.linspace(0, 4 * n_orbits, plot_steps)
            self.pos_object = self.object_orbit.xyzPos(self.t_object)

            if color == None:
                r = lambda: np.random.randint(0,255)
                self.color = '#%02X%02X%02X' % (r(),r(),r())
            else:
                self.color = color

            self.ax.set_aspect('equal')

            if sun:
                self.ax.scatter([0], [0], [0], color="yellow", s=self.sun_size, label="Sun")
            else:
                pass
            
            if self.inclination_plot:
                self.inclinationObserver(self.semi_major_axis, self.perihelion, 
                                            self.eccentricity, self.longitude_of_ascending_node, 
                                            self.inclination, self.argument_of_perihelion, 
                                            self.object_orbit, n_orbits, plot_steps)
            else:
                pass
            
            if display_name:
                current_pos = self.pos_object[0]
                self.display_name(current_pos, self.object_id, self.color, fontsize=fontsize, fontweight=fontweight)
                

            self.object_positions[self.name] = self.pos_object

            self.object_dot = self.ax.scatter([self.pos_object[0][0]], [self.pos_object[0][1]], [self.pos_object[0][2]], color=self.color, label=f"{self.name}", s=self.planet_size)

            if trajectory:
                self.ax.plot(self.pos_object[:,0], self.pos_object[:,1], self.pos_object[:,2], color=self.color, alpha=self.alpha, linewidth=1)
            else:
                pass



            self.object_dots[self.name] = self.object_dot




    def animate_before(self, i):


        for unit, object_dot in self.object_dots.items():
            pos_index = int(i) % len(self.object_positions[unit])
            pos_object = self.object_positions[unit][pos_index]

            object_dot._offsets3d = (np.array([pos_object[0]]), np.array([pos_object[1]]), np.array([pos_object[2]]))


        self.fig.canvas.draw()

        return list(self.object_dots.values())
    


    def animateOrbit(self, dpi, save=False, 
                     export_zoom=None, font_size="xx-small", 
                     export_folder=None, animation_interval=40,
                     
                     x_lim=None, y_lim=None, z_lim=None,
                     x_label="X-Axis", y_label="Y-Axis", z_label="Z-Axis"
                     
                     ):

        self.vicinity_radius = export_zoom

        myAnimation = animation.FuncAnimation(self.fig, self.animate_before, interval=animation_interval, frames=np.arange(0, self.steps), blit=True, repeat=True)

        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)
        self.ax.set_zlabel(z_label)

        self.plt.legend(loc="lower right", fontsize=font_size)
        self.plt.title(f'{self.name}')


        if save:
            # self.ax.view_init(elev=30, azim=-60)

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


    #details of singular object 
    def semiMajorAxis(self, semi_major_axis):
        self.semi_major_axis = semi_major_axis
    
    def perihelion(self, perihelion):
        self.perihelion = perihelion
    
    def eccentricity(self, eccentricity):
        self.eccentricity = eccentricity

    def inclination(self, inclination):
        self.inclination = inclination

    def longitudeOfAscendingNode(self, longitude_of_ascending_node):
        self.longitude_of_ascending_node = longitude_of_ascending_node
    
    def argumentOfPerihelion(self, argument_of_perihelion):
        self.argument_of_perihelion = argument_of_perihelion

    def sunSize(self, sun_size):
        print("sun size")
        self.sun_size = sun_size


    def planetSize(self, planet_size):
        self.planet_size = planet_size


    def inclinationPlot(self, color):
        self.inclination_plot_color = color
        self.inclination_plot = True
        
    def objectName(self, object_id):
        self.object_id = object_id
        
    def color(self, color):
        self.color = color
        

    








# test = SimpleOrbit(plot_title="Test", name="Earth", fps=30)

# #styling
# test.faceColor("black")
# test.paneColor("black")
# test.gridColor("#222831")
# test.orbitTransparency(0.5)
# test.labelColor("white")
# test.tickColor("white")

# test.plotStyle(background_color="dark_background")

# # the form of the list should be as follows: "name", semi_major_axis, perihelion, eccentricity, inclination, longitude_of_ascending_node, argument_of_perihelion, color (optional)
# data = [["object1", 1, 0.983289891, 0.01671123, 15, 0, 0, "green"], ["object2", 1.5, 0.483289891, 0.02671123, 6, 0, 0, "yellow"], ["object3", 1.3, 0.683289891, 0.01671123, 2, 0, 0, "red"]]

# # cool shape
# # data = [['electron1', 0.5, 0.45, 0.1, 10, 0, 0, 'blue'],
# #  ['electron2', 1.0, 0.9, 0.1, 20, 0, 0, 'green'],
# #  ['electron3', 1.5, 1.35, 0.1, 30, 0, 0, 'red'],
# #  ['electron4', 2.0, 1.8, 0.1, 40, 0, 0, 'yellow'],
# #  ['electron5', 2.5, 2.25, 0.1, 50, 0, 0, 'orange'],
# #  ['electron6', 3.0, 2.7, 0.1, 60, 0, 0, 'purple']]

# # cool atom shape
# # data = [
# #     ['electron1', 1.0, 0.8, 0.2, 0.0, 0, 0, 'red'],
# #     ['electron2', 1.0, 0.8, 0.2, 30.0, 0, 0, 'red'],
# #     ['electron3', 1.0, 0.8, 0.2, 60.0, 0, 0, 'red'],
# #     ['electron4', 1.0, 0.8, 0.2, 90.0, 0, 0, 'red'],
# #     ['electron5', 1.0, 0.8, 0.2, 120.0, 0, 0, 'red'],
# #     ['electron6', 1.0, 0.8, 0.2, 150.0, 0, 0, 'red']]

# # cool atom shape 2x less
# # data = [
# #     ['electron1', 1.0, 0.2, 0.6, 0.0, 0, 0, 'red'],
# #     ['electron2', 1.0, 0.2, 0.6, 60.0, 0, 0, 'red'],
# #     ['electron3', 1.0, 0.2, 0.6, 120.0, 0, 0, 'red'],
# # ]



# # you can also use the following instead of data if you want to plot a single object
# # test.semiMajorAxis(1)
# # test.perihelion(0.983289891)
# # test.eccentricity(0.01671123)
# # test.inclination(0)
# # test.longitudeOfAscendingNode(0)
# # test.argumentOfPerihelion(0)


# test.sunSize(1000)
# test.planetSize(100)

# test.inclinationPlot("white")

# test.calculateOrbit(plot_steps=1000, n_orbits=4, data=data,
#                     # color="blue",
#                     trajectory=True, sun=True, inclinationObserver=True)

# # test.drawLineTwoPoints([0, 0, 0], [200, 200, 201])
# # test.drawLineTwoPointsName("object1")

# # you can choose if you want to set boundaries for the plot
# # test.xLim([20, 20])
# # test.yLim([20, 20])
# # test.zLim([1, 1])

# test.xLabel("X-Axis")
# test.yLabel("Y-Axis")
# test.zLabel("Z-Axis")


# test.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", export_folder="results", animation_interval=10)

