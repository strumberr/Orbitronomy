## <span style="color:#857EBB;">Official Orbitronomy Library</span>

The `Orbitronomy` library offers functionality for calculating, visualizing, plotting, and animating the orbits of various celestial bodies in 3D. It utilizes Kepler's elliptical orbit equations and PyAstronomy for orbital calculations, and Matplotlib for 3D plotting.

### <span style="color:#FACBD3;">SimpleOrbit Class</span>

The `SimpleOrbit` class provides the capability of simulating single object orbits, and multiple object orbits in the format of a list within list.

#### <span style="color:#CA9DD7;">Constructor</span>

**SimpleOrbit(plot_title, name)**

##### Parameters:

- <span style="color:#CA9DD7;">plot_title</span>: Title for the plot.
- <span style="color:#CA9DD7;">name</span>: Identifier for the celestial body.

#### <span style="color:#CA9DD7;">Methods</span>

- <span style="color:#CA9DD7;">faceColor(color)</span>: Sets the face color of the axes.
- <span style="color:#CA9DD7;">paneColor(color)</span>: Sets the color of the 3D panes.
- <span style="color:#CA9DD7;">gridColor(color)</span>: Sets the grid color.
- <span style="color:#CA9DD7;">orbitTransparency(value): Sets the transparency of the orbits.
- <span style="color:#CA9DD7;">labelColor(color)</span>: Sets the color of axis labels.
- <span style="color:#CA9DD7;">tickColor(color)</span>: Sets the color of axis ticks.
- <span style="color:#CA9DD7;">plotStyle(background_color)</span>: Sets the background style of the plot.
- <span style="color:#CA9DD7;">semiMajorAxis(value), perihelion(value), eccentricity(value), inclination(value), longitudeOfAscendingNode(value), argumentOfPerihelion(value)</span>: Set specific orbital parameters.

#### Usage Example:

```python
from orbitronomy.orbitCalcs import SimpleOrbit

test = SimpleOrbit(plot_title="Test", name="Earth")

# Styling
test.faceColor("black")
test.paneColor("black")
test.gridColor("#222831")
test.orbitTransparency(0.5)
test.labelColor("white")
test.tickColor("white")

test.plotStyle(background_color="dark_background")

data = [["object1", 1, 0.983289891, 0.01671123, 15, 0, 0, "green"], ["object2", 1.5, 0.483289891, 0.02671123, 6, 0, 0, "yellow"], ["object3", 1.3, 0.683289891, 0.01671123, 2, 0, 0, "red"]]

# Calculating and plotting orbits
test.calculateOrbit(plot_steps=1000, n_orbits=1, data=data, trajectory=True, sun=True)

#you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([0.1, 0.1])

# Setting axis labels
test.xLabel("X-Axis")
test.yLabel("Y-Axis")
test.zLabel("Z-Axis")

# Animating the orbits
test.animateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small", export_folder="results")
```


## <span style="color:#857EBB;">Orbitronomy Library with Dataset Functionality</span>

The `Orbitronomy` library is enhanced with functionality to calculate, visualize, plot, and animate orbits of celestial bodies in 3D using datasets. It utilizes Kepler's elliptical orbit equations, PyAstronomy for orbital calculations, and Matplotlib for 3D plotting.

### <span style="color:#FACBD3;">datasetOrbit Class</span>

The `datasetOrbit` class extends the capabilities of the `SimpleOrbit` class, allowing for the use of datasets to plot multiple celestial bodies.

#### <span style="color:#CA9DD7;">Constructor</span>

**datasetOrbit(plot_title, name)**

##### Parameters:

- <span style="color:#CA9DD7;">plot_title</span>: Title for the plot.
- <span style="color:#CA9DD7;">name</span>: Identifier for the celestial body or simulation.

#### <span style="color:#FACBD3;">**Styling Methods**</span>

- <span style="color:#CA9DD7;">faceColor</span>(color)
- <span style="color:#CA9DD7;">paneColor</span>(color)
- <span style="color:#CA9DD7;">gridColor</span>(color)
- <span style="color:#CA9DD7;">orbitTransparency</span>(value)
- <span style="color:#CA9DD7;">labelColor</span>(color)
- <span style="color:#CA9DD7;">tickColor</span>(color)
- <span style="color:#CA9DD7;">datasetPlotStyle(background_color)

#### <span style="color:#FACBD3;">Dataset Configuration</span>

- <span style="color:#CA9DD7;">columnSemiMajorAxis</span>(column_name)
- <span style="color:#CA9DD7;">columnPerihelion</span>(column_name)
- <span style="color:#CA9DD7;">columnEccentricity</span>(column_name)
- <span style="color:#CA9DD7;">columnInclination</span>(column_name)
- <span style="color:#CA9DD7;">columnLongitudeOfAscendingNode</span>(column_name)
- <span style="color:#CA9DD7;">columnArgumentOfPerihelion</span>(column_name)
- <span style="color:#CA9DD7;">columnColor</span>(column_name)
- <span style="color:#CA9DD7;">columnName</span>(column_name)
- <span style="color:#CA9DD7;">fileName</span>(file_name)

#### <span style="color:#FACBD3;">Orbit Calculation and Animation</span>

- <span style="color:#CA9DD7;">datasetCalculateOrbit</span>(plot_steps, n_orbits, color, trajectory, sun, random_color)
- <span style="color:#CA9DD7;">xLim(lim), yLim(lim), zLim(lim)</span>
- <span style="color:#CA9DD7;">xLabel(label), yLabel(label), zLabel(label)</span>
- <span style="color:#CA9DD7;">datasetAnimateOrbit</span>(dpi, save, export_zoom, font_size, export_folder)

#### Usage Example:

```python
from orbitronomy.datasetOrbit import datasetOrbit

test = datasetOrbit(plot_title="Test", name="Earth")

# Styling
test.faceColor("black")
test.paneColor("black")
test.gridColor("#222831")
test.orbitTransparency(0.5)
test.labelColor("white")
test.tickColor("white")

test.datasetPlotStyle(background_color="dark_background")

# Dataset column configuration (the name of each column of the CSV dataset being used)
test.columnSemiMajorAxis("semi_major_axis")
test.columnSemiMajorAxis("semi_major_axis")
test.columnPerihelion("perihelion")
test.columnEccentricity("eccentricity")
test.columnInclination("inclination")
test.columnLongitudeOfAscendingNode("longitude_of_ascending_node")
test.columnArgumentOfPerihelion("argument_of_perihelion")
test.columnColor("color")
test.columnName("name")

# Specifying the dataset file name
test.fileName("datasets/Planetary-Satellite-Data.csv")

# Calculating and plotting orbits from the dataset
test.datasetCalculateOrbit(plot_steps=1000, n_orbits=12, color="yellow", random_color=True, trajectory=True, sun=True)

#you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([0.1, 0.1])

test.xLabel("X-Axis")
test.yLabel("Y-Axis")
test.zLabel("Z-Axis")

# Animating the orbits
test.datasetAnimateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small")
```