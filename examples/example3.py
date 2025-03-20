# Example: Atomic Model Visualization using SimpleOrbit
from orbitronomy import SimpleOrbit

# Initialize the plot with a title and nucleus name (e.g., "Atom")
atom_model = SimpleOrbit(plot_title="Atomic Orbitals", name="Nucleus", fps=30)

# Styling: dark background and neon-like colors for electrons
atom_model.faceColor("black")
atom_model.paneColor("black")
atom_model.gridColor("#222831")
atom_model.orbitTransparency(0.4)
atom_model.labelColor("white")
atom_model.tickColor("white")
atom_model.plotStyle(background_color="dark_background")

# Define electron orbits (simulate different energy levels)
# Each electron: [name, orbit radius, perihelion, eccentricity, inclination, 0, 0, color]
electrons = [
    ["e1", 1.0, 0.9, 0.1, 0, 0, 0, "cyan"],
    ["e2", 1.5, 1.4, 0.1, 45, 0, 0, "magenta"],
    ["e3", 2.0, 1.9, 0.1, 90, 0, 0, "yellow"],
    ["e4", 2.5, 2.4, 0.1, 135, 0, 0, "lime"]
]

# Set sizes for nucleus and electrons
atom_model.sunSize(800)       # Nucleus size
atom_model.planetSize(80)     # Electron marker size

# Optionally, plot inclination to show orbital tilts
atom_model.inclinationPlot("white")

# Calculate orbits (simulate a few full revolutions)
atom_model.calculateOrbit(plot_steps=1000, n_orbits=3, data=electrons,
                          trajectory=True, sun=True, inclinationObserver=True,
                          display_name=True, fontsize=10, fontweight="normal")

# Label axes for reference
atom_model.xLabel("X")
atom_model.yLabel("Y")
atom_model.zLabel("Z")

# Animate the plot (results in an animated GIF if saving is enabled)
atom_model.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", animation_interval=10)
