import numpy as np
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D

from datetime import date
import csv


writer = PillowWriter(fps=30)

asteroid_name = "Tons of celestial bodies"

file_name = 'datasets/Planetary-Satellite-Data.csv'


plt.style.use('dark_background')
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


ax.set_facecolor('black')

ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))

ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)


planet_dots = {}
planet_positions = {}
orbital_periods = {}

ax.scatter([0], [0], [0], color="yellow", s=100, label="Sun")

colors_planets = { "mercury": "#8c8c8c", "venus": "#ffcc66", "earth": "#66ccff", "mars": "#ff6666", "jupiter": "#ffcc00", "saturn": "#ff9900", "uranus": "#66ffff", "neptune": "#3366ff" }

with open(file_name, mode='r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    

    for row in csv_reader:
        # print(f"Plotting {row} orbit")

        unit = row['Unit (AU)']
        semi_major_axis = row['Semi-major Axis']
        perihelion = row['Perihelion']
        eccentricity = row['Eccentricity']
        inclination = row['Inclination']
        longitude_of_ascending_node = row['Longitude of ascending node']
        argument_of_perihelion = row['Argument of perihelion/periapsis/perifocus']

        planet_orbit = pyasl.KeplerEllipse(a=float(semi_major_axis), per=float(perihelion), e=float(eccentricity), Omega=float(longitude_of_ascending_node), i=float(inclination), w=float(argument_of_perihelion))
        
        t_planet = np.linspace(0, 4 * 12, 600)
        pos_planet = planet_orbit.xyzPos(t_planet)

        r = lambda: np.random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())

        print(unit.lower())

        if unit.lower() in colors_planets:
            print("Found planet color")
            color = colors_planets[unit.lower()]

        planet_positions[unit] = pos_planet

        planet_dot = ax.scatter([pos_planet[0][0]], [pos_planet[0][1]], [pos_planet[0][2]], color=color, label=f"{unit}")

        ax.plot(pos_planet[:,0], pos_planet[:,1], pos_planet[:,2], color=color, alpha=0.5, linewidth=1)

        planet_dots[unit] = planet_dot

        a = float(semi_major_axis)
        orbital_period = np.sqrt(a**3)
        orbital_periods[unit] = orbital_period






asteroid_dots = {}
asteroid_positions = {}

all_asteroids = 'datasets/all_asteroids.csv'

with open(all_asteroids, mode='r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    

    for row in csv_reader:


        asteroid = row['Name'].lower()
        number = float(row['Num'])

        if number >= 800:
            break

        semi_major_axis = float(row['a'])
        eccentricity = float(row['e'])
        inclination = float(row['i'])
        longitude_of_ascending_node = float(row['Node'])
        argument_of_perihelion = float(row['w'])
        
        if eccentricity == 1:
            print("Eccentricity is 0")
            eccentricity = 1.0000000000000001e-10

        perihelion = float(semi_major_axis) * (1 - float(eccentricity))
        
        print(f"Asteroid: {asteroid}, Semi-major Axis: {semi_major_axis} AU, Eccentricity: {eccentricity}, Inclination: {inclination}°, Longitude of Ascending Node: {longitude_of_ascending_node}°, Argument of Perihelion: {argument_of_perihelion}°, Perihelion: {perihelion} km")

        r = lambda: np.random.randint(0,255)
        color = '#%02X%02X%02X' % (r(),r(),r())

        asteroid_orbit = pyasl.KeplerEllipse(a=semi_major_axis, per=perihelion, e=eccentricity, 
                                            Omega=longitude_of_ascending_node, i=inclination, w=argument_of_perihelion)
        t_asteroid = np.linspace(0, 4 * 1, 600)
        pos_asteroid = asteroid_orbit.xyzPos(t_asteroid)

        ax.plot(pos_asteroid[:, 0], pos_asteroid[:, 1], pos_asteroid[:, 2], color=color, alpha=0.5, linewidth=0.3)

        asteroid_positions[asteroid] = pos_asteroid

        asteroid_dot = ax.scatter([pos_asteroid[0][0]], [pos_asteroid[0][1]], [pos_asteroid[0][2]], color=color)
        asteroid_dots[asteroid] = asteroid_dot


        
min_period = max(orbital_periods.values())
relative_speeds = {}

for unit, period in orbital_periods.items():
    
    relative_speed = min_period / period

    relative_speeds[unit] = relative_speed


vicinity_radius = 3


def animate(i):

    for unit, planet_dot in planet_dots.items():
        pos_index = int(i) % len(planet_positions[unit])
        pos_planet = planet_positions[unit][pos_index]

        planet_dot._offsets3d = (np.array([pos_planet[0]]), np.array([pos_planet[1]]), np.array([pos_planet[2]]))
 


    for asteroid, asteroid_dot in asteroid_dots.items():
        pos_index = int(i) % len(asteroid_positions[asteroid])
        pos_asteroid = asteroid_positions[asteroid][pos_index]

        asteroid_dot._offsets3d = (np.array([pos_asteroid[0]]), np.array([pos_asteroid[1]]), np.array([pos_asteroid[2]]))

    fig.canvas.draw()

    return list(planet_dots.values()) + list(asteroid_dots.values())


ax.set_aspect('equal')

myAnimation = animation.FuncAnimation(fig, animate, interval=40, frames=np.arange(0, 600), blit=True, repeat=True)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.legend(loc="lower right", fontsize='xx-small')
plt.title(f'{asteroid_name} Orbital Simulation')

# ax.view_init(elev=30, azim=-60)
# ax.set_xlim(-vicinity_radius, vicinity_radius)
# ax.set_ylim(-vicinity_radius, vicinity_radius)
# ax.set_zlim(-0.1, 0.1)

# myAnimation.save(f'results/{asteroid_name}-orbit2.gif', writer=writer, dpi=250)



plt.show()