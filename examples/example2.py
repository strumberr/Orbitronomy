# Example: Mini Solar System using SimpleOrbit
from orbitronomy import SimpleOrbit

# Create a SimpleOrbit object with title and name (e.g., "Solar System")
solar_system = SimpleOrbit(plot_title="Mini Solar System", name="Sun", fps=30)

# Customize plot style (dark background for a space-like feel)
solar_system.faceColor("black")
solar_system.paneColor("black")
solar_system.gridColor("#222831")
solar_system.orbitTransparency(0.6)
solar_system.labelColor("white")
solar_system.tickColor("white")
solar_system.plotStyle(background_color="dark_background")

# Define multiple celestial objects (planetary orbits) as a list.
# Each entry: [name, semi_major_axis, perihelion, eccentricity, inclination, longitude of ascending node, argument of perihelion, color]
planets = [
    ["Mercury", 0.39, 0.307, 0.205, 7, 0, 29, "gray"],
    ["Venus", 0.72, 0.718, 0.007, 3.4, 0, 54, "yellow"],
    ["Earth", 1.00, 0.983, 0.017, 0, 0, 102, "blue"]
]

# Set Sun and planet sizes for a balanced visualization
solar_system.sunSize(1200)
solar_system.planetSize(150)

# Optionally, enable an inclination plot to visualize orbital tilts
solar_system.inclinationPlot("red")

# Generate and animate the orbit over 4 full periods with a detailed step count
solar_system.calculateOrbit(plot_steps=1000, n_orbits=4, data=planets,
                            trajectory=True, sun=True, inclinationObserver=True,
                            display_name=True, fontsize=12, fontweight="normal")

# Set axis labels and optional limits for focus
solar_system.xLabel("X (AU)")
solar_system.yLabel("Y (AU)")
solar_system.zLabel("Z (AU)")
# Optionally set axis limits: solar_system.xLim([...]), etc.

# Animate the orbit (animation settings can be adjusted as needed)
solar_system.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", export_folder="results", animation_interval=10)
