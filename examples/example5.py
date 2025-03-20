# Enhanced Example: Earth Satellite Orbits Visualization using DatasetOrbit
from orbitronomy import DatasetOrbit

# Initialize the DatasetOrbit object with a meaningful title and dataset name
satellite_orbits = DatasetOrbit(plot_title="Earth Satellite Orbits", name="Satellite Data", fps=30)

# --- Styling the Plot ---
# Set colors to achieve a high-contrast, dark-space themed look
satellite_orbits.faceColor("white")         # Background of the 3D plot
satellite_orbits.paneColor("white")         # Color of the axes planes
satellite_orbits.gridColor("black")         # Color of the grid lines
satellite_orbits.orbitTransparency(1)       # Fully opaque orbit lines
satellite_orbits.labelColor("black")        # Color of axis labels
satellite_orbits.tickColor("black")         # Color of axis ticks

# Apply the dataset-specific plot style (e.g., dark background)
satellite_orbits.datasetPlotStyle(background_color="dark_background")

# --- Mapping Dataset Columns ---
# Define the names of the columns in your CSV dataset so that the library can correctly map the orbital parameters
satellite_orbits.columnSemiMajorAxis("semi_major_axis")
satellite_orbits.columnPerihelion("perihelion")
satellite_orbits.columnEccentricity("eccentricity")
satellite_orbits.columnInclination("inclination")
satellite_orbits.columnLongitudeOfAscendingNode("longitude_of_ascending_node")
satellite_orbits.columnArgumentOfPerihelion("argument_of_perihelion")
satellite_orbits.columnColor("color")
satellite_orbits.columnName("name")

# Specify the file path to your dataset
satellite_orbits.fileName("datasets/Planetary-Satellite-Data.csv")

# --- Additional Plot Settings ---
# Enable the inclination plot with a black color to visualize the orbital tilts
satellite_orbits.inclinationPlot("black")

# --- Generate the Orbit Plot ---
satellite_orbits.datasetCalculateOrbit(
    plot_steps=1000,          # Number of steps for plotting the orbits
    n_orbits=12,              # Display 12 orbital periods
    color="yellow",           # Default orbit color (overridden by random_color)
    random_color=True,        # Randomize colors for better differentiation
    trajectory=True,          # Show the full trajectory of each satellite
    sun=True,                 # Plot the Sun (or central body) at the origin
    delimiter=";",            # Delimiter used in the CSV file
    inclinationObserver=True, # Enable the observer's inclination view
    display_name=True,        # Display the names/IDs of the satellites
    fontsize=12,              # Font size for displayed names
    fontweight="normal",      # Font weight for displayed names
    fontcolor="black"         # Font color for displayed names
)

# --- Labeling and Optional Axis Boundaries ---
satellite_orbits.xLabel("X-Axis (km)")
satellite_orbits.yLabel("Y-Axis (km)")
satellite_orbits.zLabel("Z-Axis (km)")
# Optionally, set custom axis limits to focus on a region of interest:
# satellite_orbits.xLim([min_x, max_x])
# satellite_orbits.yLim([min_y, max_y])
# satellite_orbits.zLim([min_z, max_z])

# --- Animate the Orbit Plot ---
# Render the 3D animation of the orbits; set save=True to export the animation as a GIF.
satellite_orbits.datasetAnimateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small")
