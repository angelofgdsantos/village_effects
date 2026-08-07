"""
Author:
Date: 
Title: 

    Description: 

    Usage: 

    Parts:

        1.
        2.
        3.
        4.

    Inputs:
    
    Outputs:
    
"""

"""
Packages
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Globals
"""

INPUT_FOLDER = '/Users/angelosantos/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia/data/processed/'
OUTPUT_FOLDER = "data/processed/merged_panel_gamma/"

"""
Functions
"""

"""
Part 1:
"""

# call dataset
distance_agg = pd.read_csv(f'{INPUT_FOLDER}14_gamma_distance.csv')

# Explit cell_id to get x and y coordinates : truncate 6 digits for x and y floats
distance_agg['x'] = distance_agg['cell_id'].str.split('_').str[0].astype(float).round(6)
distance_agg['y'] = distance_agg['cell_id'].str.split('_').str[1].astype(float).round(6)

# New cell id 
distance_agg['pixel_id'] = distance_agg['x'].astype(str) + '_' + distance_agg['y'].astype(str)

# panel dataset
panel = pd.read_stata(f'{INPUT_FOLDER}10_pixel_panel.dta')

# Merge datasets
merge = pd.merge(panel, distance_agg[['cell_id','pixel_id','probability']], on='pixel_id', how='left')

# Drop rows with missing cell_id
merge = merge[merge.cell_id.notna()].reset_index(drop=True)

"""
Part 2: Plot both dfs to check if merge worked 
"""

# Create geometry column for distance_agg
distance_agg['geometry'] = gpd.points_from_xy(distance_agg['x'], distance_agg['y'])
distance_agg_gdf = gpd.GeoDataFrame(distance_agg, geometry='geometry')

# Panel dataset
panel_gdf = panel.groupby('pixel_id').first().reset_index()
panel_gdf['x'] = panel_gdf['pixel_id'].str.split('_').str[0].astype(float)
panel_gdf['y'] = panel_gdf['pixel_id'].str.split('_').str[1].astype(float)
panel_gdf['geometry'] = gpd.points_from_xy(panel_gdf['x'], panel_gdf['y'])
panel_gdf = gpd.GeoDataFrame(panel_gdf, geometry='geometry')

# Map
fig, ax = plt.subplots(figsize=(10, 10))
distance_agg_gdf.plot(ax=ax, markersize=1, color='blue', alpha=0.5)
panel_gdf.plot(ax=ax, markersize=1, color='red', alpha=0.5)
plt.savefig(f'{OUTPUT_FOLDER}15_merge_check.png', dpi=300, bbox_inches='tight')

"""
Part 3: Save data
"""

merge.to_csv(f'{OUTPUT_FOLDER}15_panel_gamma_distance.csv', index=False)
merge.to_stata(f'{OUTPUT_FOLDER}15_panel_gamma_distance.dta', write_index=False)