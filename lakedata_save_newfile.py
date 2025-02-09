import os
import osmnx as ox
from osmnx._errors import InsufficientResponseError
import cv2
import numpy as np
import shutil
import pandas as pd
from pyproj import Transformer




def saveandprocess(north, south, east, west):

    tags = {"natural": "water", "water": "lake"}
    lake_data = pd.DataFrame()

    print("Downloading lake data...")
    #Get the data from API
    try:
        lake_data = ox.geometries_from_bbox(north, south, east, west, tags)
    except InsufficientResponseError:
        print(" No lakes in the ENTIRE box")

    output_folder = "osm_lakecontours"
    #shutil.rmtree(output_folder, ignore_errors=True)
    os.makedirs(output_folder, exist_ok=True)

    if not lake_data.empty:
        print(f"Found {len(lake_data)} geometries, filtering polygons...")
        # keep original geometries for centroid calculation
        lakes = lake_data[lake_data.geometry.type == "Polygon"].copy()
        lakes_utm = lakes.to_crs(epsg=32633)  # reproject to UTM

        # prepare transformer to convert UTM centroids back to WGS84
        transformer = Transformer.from_crs(lakes_utm.crs, "EPSG:4326", always_xy=True)

        for idx, lake in lakes_utm.iterrows():
            if lake.geometry.area > 2500:
                # get centroid in UTM and convert to WGS84
                centroid_utm = lake.geometry.centroid
                lon, lat = transformer.transform(centroid_utm.x, centroid_utm.y)

                # do not include lakes that keep continue outside the boundaries
                if not (south <= lat <= north and west <= lon <= east):
                    continue

                # create image and draw contours
                print(f"Processing lake at ({lat:.6f}, {lon:.6f})...")
                img = np.zeros((384, 384), dtype=np.uint8)
                bounds = lake.geometry.bounds
                minx, miny, maxx, maxy = bounds
                scale_x = 384 / (maxx - minx)
                scale_y = 384 / (maxy - miny)

                for polygon in lake.geometry.geoms if lake.geometry.geom_type == "MultiPolygon" else [lake.geometry]:
                    contours = np.array([
                        (int((x - minx) * scale_x), 384 - int((y - miny) * scale_y))
                        for x, y in polygon.exterior.coords
                    ], dtype=np.int32)
                    cv2.drawContours(img, [contours], -1, 255, 2)

                # save with WGS84 centroid coordinates
                lake_filename = f"lake_{lat:.6f}_{lon:.6f}.png"
                cv2.imwrite(os.path.join(output_folder, lake_filename), img)
                print(f"Saved image: {lake_filename}")
            else:
                centroid_utm = lake.geometry.centroid
                lon, lat = transformer.transform(centroid_utm.x, centroid_utm.y)
                print(f"lake at {lat:.6f} {lon:.6f} too small")
    else:
        print("No lake data found.")

# missing from 61.5 to 61
#saveandprocess(61.125, 61.0, 25.125, 25.0)
