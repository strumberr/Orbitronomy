# Tests for the keppler_elements.py module
from orbitronomy import DatasetOrbit


test = DatasetOrbit(plot_title="Test", name="Earth")


#styling
test.faceColor("white")
test.paneColor("white")
test.gridColor("black")
test.orbitTransparency(1)
test.labelColor("black")
test.tickColor("black")


test.datasetPlotStyle(background_color="dark_background")


#name of the columns in the dataset in CSV format
test.columnSemiMajorAxis("semi_major_axis")
test.columnPerihelion("perihelion")
test.columnEccentricity("eccentricity")
test.columnInclination("inclination")
test.columnLongitudeOfAscendingNode("longitude_of_ascending_node")
test.columnArgumentOfPerihelion("argument_of_perihelion")
test.columnColor("color")
test.columnName("name")

#name of the dataset file
test.fileName("datasets/Planetary-Satellite-Data.csv")

test.inclinationPlot("black")


test.datasetCalculateOrbit(plot_steps=1000, n_orbits=12, color="yellow", 
                    random_color=True, trajectory=True, sun=True, delimiter=";",
                    inclinationObserver=True, 
                    display_name=True, fontsize=12, fontweight="normal", fontcolor="black")


#you can choose if you want to set boundaries for the plot
# test.xLim([20, 20])
# test.yLim([20, 20])
# test.zLim([0.1, 0.1])

test.xLabel("X-Axis")
test.yLabel("Y-Axis")
test.zLabel("Z-Axis")

test.datasetAnimateOrbit(dpi=250, save=False, export_zoom=3, font_size="xx-small")

