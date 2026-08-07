"""
Author: Angelo Santos
Date: 2024
Title: Cell-Buffer Distance Calculator

    Description: 
    This script calculates distances between raster cells and walking distance buffers 
    for analyzing local effects of deforestation in Zambia. It processes cell coordinates
    and buffer geometries to compute spatial relationships and distances.

    Usage: 
    Run the script to process cell-buffer distance calculations in chunks and combine results.
    Modify input paths and chunk parameters as needed for your specific dataset.

    Parts:

        1. Call datasets : Raw cell and buffers
        2. Exctracting cells
        3. Call csv with cell coordinates
        4. Save dataset
        5. Combine chunks

    Inputs:
    - WalkingDistanceForestBuffer.shp: Shapefile containing buffer geometries with 'vilid' and 'dforest' attributes
    - pixel_weights.csv: CSV file with cell coordinates (x, y) and total_weight values
    
    Outputs:
    - 13_distances_chunk{i}.csv: Individual chunk files with cell-buffer distances
    - 13_distances.csv: Combined final dataset with all cell-buffer distance calculations
    
"""

"""
Packages
"""

import numpy as np
import pandas as pd
import rasterio
from rasterio.features import geometry_mask
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

"""
Globals
"""

input_cells = '/Users/angelosantos/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia/data/Rasters'
input_buffers = '/Users/angelosantos/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia/data/project area/WalkingData'
input_cells_filtered = '/Users/angelosantos/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia/data/processed'

"""
Functions
"""

"""
Part 1: Call datasets : Raw cell and buffers
"""

# Cells data : Zambia_East_10s_030E_Cover_Aligned.tif
with rasterio.open(f'{input_cells}/Zambia_East_10s_030E_Cover_Aligned.tif') as src:
        raster_data = src.read(1)
        transform = src.transform
        crs = src.crs
        height, width = raster_data.shape

# Walking distance buffers data : WalkingDistanceForestBuffer.shp
buffers_gdf = gpd.read_file(f'{input_buffers}/WalkingDistanceForestBuffer.shp')
buffers_gdf['geometry'] = buffers_gdf.centroid.buffer(10000)

# Reproject buffers to match raster to degrees
crs = rasterio.crs.CRS.from_epsg(4326)  # WGS 84
buffers_gdf = buffers_gdf.to_crs(crs)

"""
Part 2: Extracting cells
"""

if buffers_gdf.crs != crs:
    buffers_gdf = buffers_gdf.to_crs(crs)

# if 'dforest' not in buffers_gdf.columns:
#     raise ValueError("Buffer shapefile must contain a 'dforest' column")

# Create weight accumulation array
weight_array = np.zeros_like(raster_data, dtype=float)

# For each buffer, rasterize it and add its distance to overlapping pixels
for idx, row in buffers_gdf.iterrows():
    # Create mask for this buffer
    mask = geometry_mask(
        [row.geometry],
        transform=transform,
        invert=True,
        out_shape=(height, width)
    )
    
    # Add buffer distance to pixels within this buffer
    if row['dforest'] > 0:
        weight_array[mask] += row['dforest']
    else:
        weight_array[mask] += 1  # Assign weight of 1 if dforest is 0 or negative : This avoids the missing cells

# Extract x, y coordinates and weights for pixels with weight > 0
rows, cols = np.where(weight_array > 0)

# Check if there are any pixels with weight 

results = []
for row, col in zip(rows, cols):
    x, y = rasterio.transform.xy(transform, row, col, offset='center')
    results.append({
        'x': x,
        'y': y,
        'total_weight': weight_array[row, col]
    })

results = pd.DataFrame(results)
results['cell_id'] = results.apply(lambda row: f"{row['x']}_{row['y']}", axis=1)
results.to_csv(f'{input_cells_filtered}/13_pixel_10km.csv', index=False)

# Plot cells 
plt.scatter(results['x'], results['y'], marker='o', color='black', s=1, alpha=0.5)

# Delete objects to free memory
del raster_data, weight_array, results, cols, mask, rows

"""
Part 3: Call csv with cell coordinates
"""

# Cell coordinates
cell_filtered = pd.read_csv(f'{input_cells_filtered}/13_pixel_10km.csv')

# Create geometry column from x and y
cell_filtered['geometry'] = cell_filtered.apply(lambda row: Point(row['x'], row['y']), axis=1)

# Drop x,y, total_weight columns
cell_filtered = cell_filtered.drop(columns=['x', 'y', 'total_weight'])

# Define GeoDataFrame with geometry and CRS
cell_filtered = gpd.GeoDataFrame(cell_filtered, geometry='geometry', crs=buffers_gdf.crs)

# Process cells in chunks and save each chunk
chunk_size = 500000
total_cells = len(cell_filtered)
num_chunks = (total_cells + chunk_size - 1) // chunk_size  # Calculate number of chunks needed

for chunk_idx in range(num_chunks):
    print(f"Processing chunk {chunk_idx + 1} of {num_chunks}")
    start_idx = chunk_idx * chunk_size
    end_idx = min((chunk_idx + 1) * chunk_size, total_cells)
    
    # Get current chunk
    cell_sample = cell_filtered[start_idx:end_idx]
    
    print(f"Processing chunk {chunk_idx + 1} of {num_chunks} (cells {start_idx} to {end_idx-1})")
    
    # Calculate distance from each cell to each buffer that intersects with the cell geometry
    distances = []
    for idx, cell in cell_sample.iterrows():
        print(f"Processing cell {idx+1} of {len(cell_sample)} in chunk {chunk_idx + 1}")
        cell_geom = cell.geometry
        # Find intersecting buffers
        intersecting_buffers = buffers_gdf[buffers_gdf.intersects(cell_geom)]
        for _, buffer in intersecting_buffers.iterrows():
            # Calculate distance between cell and buffer
            distance = cell_geom.distance(buffer.geometry.centroid)
            distances.append({
                'cell_id': cell['cell_id'],
                'vilid': buffer['vilid'],
                'distance': distance
            })

    distances_df = pd.DataFrame(distances)

    """
    Part 4: Save dataset
    """

    # Save distances to csv for each chunk
    distances_df.to_csv(f'{input_cells_filtered}/13_distances_chunk{chunk_idx + 1}.csv', index=False)
    print(f"Saved chunk {chunk_idx + 1} with {len(distances_df)} distance records")

    # Delete objects before starting next chunk
    del cell_sample 
    del distances_df

"""
Part 5: Combine chunks
"""

del cell_filtered

# Read all chunks and combine them
num_chunks = 25  # Update this if you have a different number of chunks

chunks = []
for i in range(1, num_chunks + 1):
    chunk = pd.read_csv(f'{input_cells_filtered}/13_distances_chunk{i}.csv')
    chunks.append(chunk)

distances_combined = pd.concat(chunks, ignore_index=True)
distances_combined.to_csv(f'{input_cells_filtered}/13_distances.csv', index=False)

print("All chunks combined successfully!")

