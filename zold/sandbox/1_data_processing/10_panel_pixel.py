"""
Author: Angelo dos Santos
Date: 2025-08-29
Title: Creating Pixel Panel

    Description: 
        Expand pixel dataset into yearly panel (2001–2024).
        Keep tree cover constant per pixel. Generate yearly
        forest loss indicator based on lossyear. 

    Usage: 
        Change root directory to your local path.

    Parts:
        1. Call pixel data and basic cleaning 
        2. Expand into panel dataset 2001–2024
        3. Generate loss indicator
        4. Save output

    Inputs:
        Zambia_East_10s_030E_ForestBuffer_PixelPanel.dta
    
    Outputs:
        Zambia_East_10s_030E_ForestBuffer_PixelPanel_panel.parquet
"""

"""
Packages
"""
import numpy as np
import pandas as pd
import geopandas as gpd

"""
Globals
"""

user = "angelosantos"
root = f"/Users/{user}/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia"
input = "/data/LossPixelPanel"
output = '/data/processed'

"""
Functions
"""

def loss_indicator(row):
    """
    Function to create loss indicator (5 minutes and 4 seconds for the all data)
    """
    if row["lossyear"] == 0:
        return 0
    elif row["year"] < row["lossyear"]:
        return 0
    elif row["year"] >= row["lossyear"]:
        return 1
    
"""
Part 1: Call pixel data and basic cleaning 
"""
# Call pixel data
pixel = pd.read_stata(f"{root}{input}/Zambia_East_10s_030E_ForestBuffer_PixelPanel.dta")

# Creating pixel id column
pixel["pixel_id"] = pixel["x"].astype(str) + "_" + pixel["y"].astype(str)

# Drop lat and lon columns
pixel = pixel.drop(columns=["x", "y"])

"""
Part 2: Create panel 2001–2024
"""
years = np.arange(2001, 2025)
panel = (
    pixel.assign(key=1)
         .merge(pd.DataFrame({"year": years, "key": 1}), on="key")
         .drop(columns="key")
)

"""
Part 3: Generate yearly loss indicator
"""

# Apply function to create loss indicator (5 minutes and 4 seconds for the all data)
panel["loss"] = panel.apply(loss_indicator, axis=1)

"""
Part 4: Save output
"""
panel.to_stata(f"{root}{output}/10_pixel_panel.dta", version=117, write_index=False)

