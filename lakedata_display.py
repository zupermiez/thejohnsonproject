import osmnx as ox
import matplotlib.pyplot as plt
from pyproj import Geod

# Define box in decimal degrees
nw_lat, nw_lon = 60.5, 25.0
se_lat, se_lon = 60.0, 26.0

geod = Geod(ellps="WGS84")
width = geod.inv(nw_lon, nw_lat, se_lon, nw_lat)[2]
height = geod.inv(nw_lon, nw_lat, nw_lon, se_lat)[2]

tags = {"natural": "water", "water": "lake"}

print("Downloading lake data")
lake_data = ox.geometries_from_bbox(nw_lat, se_lat, se_lon, nw_lon, tags)

if not lake_data.empty:
    lakes = lake_data[lake_data.geometry.type == "Polygon"]

    fig, ax = plt.subplots(figsize=(16, 16))
    lakes.plot(ax=ax, color="blue", edgecolor="black")
    plt.title(f"Lakes in Box ({width:.2f}m x {height:.2f}m)", fontsize=20)
    plt.axis("off")
    plt.show()

    lakes.to_file("lakes.geojson", driver="GeoJSON")
    print("Lakes saved to lakes.geojson.")
else:
    print("No lake data found.")
