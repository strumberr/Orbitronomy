import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
from datetime import date
import csv
from ..ingredientes.features import *


class ParentChildOrbit(FeaturesExtra):
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
        self.label_color = "black"
        self.tick_color = "black"

        self.alpha_parent_object = 1
        self.alpha_child_object = 1

        self.parent_object_size = 100
        self.child_object_size = 100

        self.orbit_transparency_parent_object = 1
        self.orbit_transparency_child_object = 1

        self.color_parent_object = "blue"
        self.color_parent_object_orbit = "green"

        self.color_child_object = "red"
        self.color_child_object_orbit = "white"

        self.sun_size = 100




        



    def plotStyle(self, background_color):

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
        

        self.alpha_parent_object = self.orbit_transparency_parent_object
        self.alpha_child_object = self.orbit_transparency_child_object

        
    
    def calculateOrbit(self, plot_steps, n_orbits_child=1, data=None, 
                       color=None, trajectory=False, sun=True, 
                       child_trajectory=True, n_orbits_parent=1):
        

        if sun:
            self.ax.scatter([0], [0], [0], color="yellow", s=self.sun_size, label="Sun")
        else:
            pass
        

        self.steps = plot_steps
        self.semi_major_axis_parent_object = self.semi_major_axis_parent_object
        self.perihelion_parent_object = self.perihelion_parent_object
        self.eccentricity_parent_object = self.eccentricity_parent_object

        if self.eccentricity_parent_object == 1:
            self.eccentricity_parent_object = 1.0000000000000001e-10

        self.inclination_parent_object = self.inclination_parent_object
        self.longitude_of_ascending_node_parent_object = self.longitude_of_ascending_node_parent_object
        self.argument_of_perihelion_parent_object = self.argument_of_perihelion_parent_object

        self.object_orbit_parent = pyasl.KeplerEllipse(a=float(self.semi_major_axis_parent_object), per=float(self.perihelion_parent_object), e=float(self.eccentricity_parent_object), Omega=float(self.longitude_of_ascending_node_parent_object), i=float(self.inclination_parent_object), w=float(self.argument_of_perihelion_parent_object))

        self.t_object_parent = np.linspace(0, 4 * n_orbits_parent, plot_steps)
        self.pos_object_parent = self.object_orbit_parent.xyzPos(self.t_object_parent)

        # if self.inclination_plot:
        #     self.inclinationObserver(self.semi_major_axis_parent_object, self.perihelion_parent_object, 
        #                                 self.eccentricity_parent_object, self.longitude_of_ascending_node_parent_object, 
        #                                 self.inclination_parent_object, self.argument_of_perihelion_parent_object, 
        #                                 self.t_object_parent, n_orbits_parent, self.steps)
        # else:
        #     pass
        
        if color == None:
            r = lambda: np.random.randint(0,255)
            self.color = '#%02X%02X%02X' % (r(),r(),r())
        else:
            self.color = color

        self.ax.set_aspect('equal')

        # self.ax.scatter([self.pos_object_parent[0][0]], [self.pos_object_parent[0][1]], [self.pos_object_parent[0][2]], color=self.color, label=f"{self.name}", s=self.planet_size)

        # child object
        self.child_orbit = pyasl.KeplerEllipse(a=float(self.semi_major_axis_child_object), 
                                            e=float(self.eccentricity_child_object), 
                                            per=float(self.perihelion_child_object), 
                                            i=float(self.inclination_child_object), 
                                            Omega=float(self.longitude_of_ascending_node_child_object), 
                                            w=float(self.argument_of_perihelion_child_object))
        
        self.t_child_object = np.linspace(0, 4 * n_orbits_child, plot_steps)
        self.pos_child_object = self.child_orbit.xyzPos(self.t_child_object)

        self.pos_child_object_relative = np.array([self.pos_child_object[j] + self.pos_object_parent[j] for j in range(len(self.t_child_object))])

        if child_trajectory:
            self.ax.plot(self.pos_child_object_relative[:, 1], self.pos_child_object_relative[:, 0], 0, label="Object Trajectory", color=self.color_child_object_orbit, linewidth=1, alpha=self.alpha_child_object)
        else:
            pass

        if trajectory:
            # self.ax.plot(self.pos_object_parent[:,0], self.pos_object_parent[:,1], self.pos_object_parent[:,2], color=self.color, alpha=self.alpha, linewidth=1)
            self.ax.plot(self.pos_object_parent[:, 1], self.pos_object_parent[:, 0], 0, label="Parent Object Trajectory", color=self.color_parent_object_orbit, alpha=self.alpha_parent_object, linewidth=1)

        else:
            pass

        # Scatter plot for Earth and Moon in 3D
        self.red_dot2 = self.ax.scatter([self.pos_object_parent[0][1]], [self.pos_object_parent[0][0]], [0], color=self.color_parent_object, label="Parent Object", s=self.parent_object_size)  # Earth
        self.red_dot3 = self.ax.scatter([self.pos_child_object_relative[0][1]], [self.pos_child_object_relative[0][0]], [0], color=self.color_child_object, label="Child Object", s=self.child_object_size)  # Moon









    def animate_before(self, i):

        self.red_dot2._offsets3d = (np.array([self.pos_object_parent[i][1]]), np.array([self.pos_object_parent[i][0]]), np.array([0]))  # Earth
        self.red_dot3._offsets3d = (np.array([self.pos_child_object_relative[i][1]]), np.array([self.pos_child_object_relative[i][0]]), np.array([0]))  # Moon
        
        self.fig.canvas.draw()

        return self.red_dot2, self.red_dot3
    


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
                print("Saving animation in filepath: ", f"{export_folder}/{self.name}-orbit.gif")
                myAnimation.save(f'{export_folder}/{self.name}-orbit.gif', writer=self.writer, dpi=dpi)
            else:
                print("Saving animation in filepath: ", f"{self.name}-orbit.gif")
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

    def labelColor(self, label_color):
        self.label_color = label_color

    def tickColor(self, tick_color):
        self.tick_color = tick_color


    #details of singular object 
    def semiMajorAxisParentObject(self, semi_major_axis):
        self.semi_major_axis_parent_object = semi_major_axis
    
    def perihelionParentObject(self, perihelion):
        self.perihelion_parent_object = perihelion
    
    def eccentricityParentObject(self, eccentricity):
        self.eccentricity_parent_object = eccentricity

    def inclinationParentObject(self, inclination):
        self.inclination_parent_object = inclination

    def longitudeOfAscendingNodeParentObject(self, longitude_of_ascending_node):
        self.longitude_of_ascending_node_parent_object = longitude_of_ascending_node
    
    def argumentOfPerihelionParentObject(self, argument_of_perihelion):
        self.argument_of_perihelion_parent_object = argument_of_perihelion

    def orbitTransparencyParentObject(self, orbit_transparency_parent_object):
        self.orbit_transparency_parent_object = orbit_transparency_parent_object

    def colorParentObjectOrbit(self, color_parent_object_orbit):
        self.color_parent_object = color_parent_object_orbit[0]
        self.color_parent_object_orbit = color_parent_object_orbit[1]




    def semiMajorAxisChildObject(self, semi_major_axis):
        self.semi_major_axis_child_object = semi_major_axis

    def perihelionChildObject(self, perihelion):
        self.perihelion_child_object = perihelion

    def eccentricityChildObject(self, eccentricity):
        self.eccentricity_child_object = eccentricity

    def inclinationChildObject(self, inclination):
        self.inclination_child_object = inclination

    def longitudeOfAscendingNodeChildObject(self, longitude_of_ascending_node):
        self.longitude_of_ascending_node_child_object = longitude_of_ascending_node

    def argumentOfPerihelionChildObject(self, argument_of_perihelion):
        self.argument_of_perihelion_child_object = argument_of_perihelion

    def orbitTransparencyChildObject(self, orbit_transparency_child_object):
        self.orbit_transparency_child_object = orbit_transparency_child_object

    def colorChildObjectOrbit(self, color_child_object_orbit):
        self.color_child_object = color_child_object_orbit[0]
        self.color_child_object_orbit = color_child_object_orbit[1]
        


    def sunSize(self, sun_size):
        self.sun_size = sun_size

    def parentObjectSize(self, parent_object_size):
        self.parent_object_size = parent_object_size

    def childObjectSize(self, child_object_size):
        self.child_object_size = child_object_size


    def inclinationPlot(self, color):
        self.inclination_plot_color = color
        self.inclination_plot = True
    








# test = ParentChildOrbit(plot_title="Test", name="Earth", fps=30)

# #styling
# test.faceColor("black")
# test.paneColor("black")
# test.gridColor("#222831")
# test.labelColor("white")
# test.tickColor("white")

# #orbit transparency for object and orbit respectively
# test.orbitTransparencyParentObject(0.5)
# test.orbitTransparencyChildObject(0.5)

# #parent object colors for object and orbit respectively
# test.colorParentObjectOrbit(["blue", "green"])

# #child object colors for object and orbit respectively
# test.colorChildObjectOrbit(["red", "white"])

# # plot style (has to be run after all styling is done)
# test.plotStyle(background_color="dark_background")


# # parent object keplerian elements
# test.semiMajorAxisParentObject(1)
# test.perihelionParentObject(0.983289891)
# test.eccentricityParentObject(0.01671123)
# test.inclinationParentObject(0)
# test.longitudeOfAscendingNodeParentObject(0)
# test.argumentOfPerihelionParentObject(0)

# # child object keplerian elements
# test.semiMajorAxisChildObject(0.4)
# test.perihelionChildObject(0.45)
# test.eccentricityChildObject(0.1)
# test.inclinationChildObject(10)
# test.longitudeOfAscendingNodeChildObject(0)
# test.argumentOfPerihelionChildObject(0)


# test.sunSize(100)

# # parent object size
# test.parentObjectSize(100)

# # child object size
# test.childObjectSize(100)

# # calculateOrbit takes the following arguments + some other ones in documentation
# test.calculateOrbit(plot_steps=1000, n_orbits_child=3,
#                     # color="blue",
#                     n_orbits_parent=1,
#                     trajectory=True, sun=True, child_trajectory=True)


# # you can choose if you want to set boundaries for the plot
# # test.xLim([20, 20])
# # test.yLim([20, 20])
# # test.zLim([1, 1])

# # you can choose if you want to set labels for the plot
# test.xLabel("X-Axis")
# test.yLabel("Y-Axis")
# test.zLabel("Z-Axis")


# test.animateOrbit(dpi=250, save=False, export_zoom=3, export_folder="results", font_size="xx-small", animation_interval=10)
