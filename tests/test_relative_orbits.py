# Tests for the keppler_elements.py module

from orbitronomy import RelativeOrbit


test = RelativeOrbit(plot_title="Test", name="Earth", fps=30)

#styling
test.faceColor("black")
test.paneColor("black")
test.gridColor("#222831")
test.labelColor("white")
test.tickColor("white")

#orbit transparency for object and orbit respectively
test.orbitTransparencyParentObject(0.5)
test.orbitTransparencyChildObject(0.5)

#parent object colors for object and orbit respectively
test.colorParentObjectOrbit(["blue", "green"])

#child object colors for object and orbit respectively
test.colorChildObjectOrbit(["red", "white"])

# plot style (has to be run after all styling is done)
test.plotStyle(background_color="dark_background")


# parent object keplerian elements
test.semiMajorAxisParentObject(1)
test.perihelionParentObject(0.983289891)
test.eccentricityParentObject(0.01671123)
test.inclinationParentObject(0)
test.longitudeOfAscendingNodeParentObject(0)
test.argumentOfPerihelionParentObject(0)

# child object keplerian elements
test.semiMajorAxisChildObject(0.4)
test.perihelionChildObject(0.45)
test.eccentricityChildObject(0.1)
test.inclinationChildObject(10)
test.longitudeOfAscendingNodeChildObject(0)
test.argumentOfPerihelionChildObject(0)


test.sunSize(100)

# parent object size
test.parentObjectSize(100)

# child object size
test.childObjectSize(100)

# calculateOrbit takes the following arguments + some other ones in documentation
test.calculateOrbit(plot_steps=1000, n_orbits_child=3,
                    # color="blue",
                    n_orbits_parent=1,
                    trajectory=True, sun=True, child_trajectory=True)


# you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([1, 1])

# you can choose if you want to set labels for the plot
test.xLabel("X-Axis")
test.yLabel("Y-Axis")
test.zLabel("Z-Axis")


test.animateOrbit(dpi=250, save=False, export_zoom=3, export_folder="results", font_size="xx-small", animation_interval=10)
