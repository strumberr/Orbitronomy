
# from orbitronomy import SimpleOrbit
from orbitronomy import SimpleOrbit

test = SimpleOrbit(plot_title="Test", name="Earth")


#styling
test.faceColor("black")
test.paneColor("black")
test.gridColor("#222831")
test.orbitTransparency(0.5)
test.labelColor("white")
test.tickColor("white")

test.plotStyle(background_color="dark_background")

# the form of the list should be as follows: "name", semi_major_axis, perihelion, eccentricity, inclination, longitude_of_ascending_node, argument_of_perihelion, color (optional)
data = [["object1", 1, 0.983289891, 0.01671123, 15, 0, 0, "green"], ["object2", 1.5, 0.483289891, 0.02671123, 6, 0, 0, "yellow"], ["object3", 1.3, 0.683289891, 0.01671123, 2, 0, 0, "red"]]

# cool shape
# data = [['electron1', 0.5, 0.45, 0.1, 10, 0, 0, 'blue'],
#  ['electron2', 1.0, 0.9, 0.1, 20, 0, 0, 'green'],
#  ['electron3', 1.5, 1.35, 0.1, 30, 0, 0, 'red'],
#  ['electron4', 2.0, 1.8, 0.1, 40, 0, 0, 'yellow'],
#  ['electron5', 2.5, 2.25, 0.1, 50, 0, 0, 'orange'],
#  ['electron6', 3.0, 2.7, 0.1, 60, 0, 0, 'purple']]

# cool atom shape
# data = [
#     ['electron1', 1.0, 0.8, 0.2, 0.0, 0, 0, 'red'],
#     ['electron2', 1.0, 0.8, 0.2, 30.0, 0, 0, 'red'],
#     ['electron3', 1.0, 0.8, 0.2, 60.0, 0, 0, 'red'],
#     ['electron4', 1.0, 0.8, 0.2, 90.0, 0, 0, 'red'],
#     ['electron5', 1.0, 0.8, 0.2, 120.0, 0, 0, 'red'],
#     ['electron6', 1.0, 0.8, 0.2, 150.0, 0, 0, 'red']]

# cool atom shape 2x less
# data = [
#     ['electron1', 1.0, 0.2, 0.6, 0.0, 0, 0, 'red'],
#     ['electron2', 1.0, 0.2, 0.6, 60.0, 0, 0, 'red'],
#     ['electron3', 1.0, 0.2, 0.6, 120.0, 0, 0, 'red'],
# ]



# you can also use the following instead of data if you want to plot a single object
# test.semiMajorAxis(1)
# test.perihelion(0.983289891)
# test.eccentricity(0.01671123)
# test.inclination(0)
# test.longitudeOfAscendingNode(0)
# test.argumentOfPerihelion(0)
# test.color("green")
# test.objectName("object1")


test.sunSize(1000)
test.planetSize(100)

test.inclinationPlot("white")

test.calculateOrbit(plot_steps=1000, n_orbits=4, data=data,
                    # color="blue",
                    trajectory=True, sun=True, 
                    inclinationObserver=True, 
                    display_name=True, fontsize=12, fontweight="normal")

# test.drawLineTwoPoints([0, 0, 0], [200, 200, 201])
# test.drawLineTwoPointsName("object1")

# you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([1, 1])

test.xLabel("X-Axis")
test.yLabel("Y-Axis")
test.zLabel("Z-Axis")


test.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", export_folder="results", animation_interval=10)


print("testing!!!!")