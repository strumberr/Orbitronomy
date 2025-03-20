# Example: Binary Star System with a Planet using RelativeOrbit
from orbitronomy import RelativeOrbit

# Initialize the RelativeOrbit object
binary_system = RelativeOrbit(plot_title="Binary Star System", name="Primary Star", fps=30)

# Styling for a space scene
binary_system.faceColor("black")
binary_system.paneColor("black")
binary_system.gridColor("#222831")
binary_system.labelColor("white")
binary_system.tickColor("white")

# Set orbit transparency for both parent (primary star) and child (secondary star)
binary_system.orbitTransparencyParentObject(0.5)
binary_system.orbitTransparencyChildObject(0.5)

# Define colors for the parent and child orbits
binary_system.colorParentObjectOrbit(["blue", "green"])
binary_system.colorChildObjectOrbit(["red", "orange"])

# Set Keplerian elements for the primary star (parent object)
binary_system.semiMajorAxisParentObject(1.0)
binary_system.perihelionParentObject(0.95)
binary_system.eccentricityParentObject(0.05)
binary_system.inclinationParentObject(0)
binary_system.longitudeOfAscendingNodeParentObject(0)
binary_system.argumentOfPerihelionParentObject(0)

# Set Keplerian elements for the secondary star (child object)
binary_system.semiMajorAxisChildObject(0.4)
binary_system.perihelionChildObject(0.38)
binary_system.eccentricityChildObject(0.1)
binary_system.inclinationChildObject(15)
binary_system.longitudeOfAscendingNodeChildObject(0)
binary_system.argumentOfPerihelionChildObject(0)

# Set sizes for the Sun (or central mass), primary star, and secondary star
binary_system.sunSize(100)         # For context, if using a central reference
binary_system.parentObjectSize(150)
binary_system.childObjectSize(120)

# Generate orbits: primary star completes 1 orbit while the secondary does 3
binary_system.calculateOrbit(plot_steps=1000, n_orbits_child=3, n_orbits_parent=1,
                             trajectory=True, sun=True, child_trajectory=True)

# Label the axes
binary_system.xLabel("X (ly)")
binary_system.yLabel("Y (ly)")
binary_system.zLabel("Z (ly)")

# Animate the binary system
binary_system.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", export_folder="results", animation_interval=10)
