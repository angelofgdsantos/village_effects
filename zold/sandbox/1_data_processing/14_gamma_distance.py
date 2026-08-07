"""
Author: Angelo dos Santos  
Date: 2026-02-07
Title: Gamma distribution distances

    Description: 
    This script applies gamma distribution cumulative distribution functions (CDF) to distance data.
    It transforms raw distance measurements into probability values using village-specific gamma parameters,
    then aggregates these transformed distances by cell ID for spatial analysis.

    Usage: 
    Run this script to process distance data through gamma distribution transformation.
    Requires input files: 13_distances.csv and 11_village_forest_gamma_params.csv
    Outputs aggregated gamma distance data to 14_gamma_distance.csv

    Parts:

        1. Call datasets : distance and gamma distribution
        2. Apply gamma distribution to distance data
        3. Plot probability of exposure to deforestation based on gamma distance

    Inputs:
    - 13_distances.csv: Contains distance measurements with village IDs and cell IDs
    - 11_village_forest_gamma_params.csv: Contains gamma distribution parameters (shape, scale) for each village
    
    Outputs:
    - 14_gamma_distance.csv: Aggregated gamma distance values by cell ID
    
"""

"""
Packages
"""

import numpy as np
import pandas as pd
from scipy.stats import gamma
import matplotlib.pyplot as plt

"""
Globals
"""

gamma_folder = '/Users/angelosantos/UH-ECON Dropbox/Angelo Santos/village_effects/data/output'
distance_folder = '/Users/angelosantos/Library/CloudStorage/Box-Box/Local_effects_deforestation_Zambia/data/processed'

"""
Functions
"""

# Apply cdf function to distance data using gamma parameters from gamma_df
def apply_gamma_cdf(row):
    village_id = row['vilid']
    try:
        shape = gamma_df.loc[gamma_df['vilid'] == village_id, 'gamma_shape'].values[0]
        scale = gamma_df.loc[gamma_df['vilid'] == village_id, 'gamma_scale'].values[0]
        return gamma.cdf(row['distance'], a=shape, scale=scale)

    except:
        shape = np.nan
        scale = np.nan
        return np.nan
    
"""
Part 1: Call datasets : distance and gamma distribution
"""

# Distance data : distance_data.csv
distance_df = pd.read_csv(f'{distance_folder}/13_distances.csv')

# Gamma distribution data : 11_CFP_HH_forest_gamma_params.csv
gamma_df = pd.read_csv(f'{gamma_folder}/11_village_forest_gamma_params.csv')

"""
Part 2: Apply gamma distribution to distance data
"""

# Apply the function to create a new column 'gamma_distance'
distance_df['gamma_distance'] = distance_df.apply(apply_gamma_cdf, axis=1)
distance_df['probability'] = 1 -  distance_df['gamma_distance']

# Save 
distance_df.to_csv(f'{distance_folder}/14_all_distances.csv')

# Aggregate by cell id : sum of gamma_distance
distance_agg = distance_df.groupby('cell_id')['probability'].sum().reset_index()

# Save results
distance_agg.to_csv(f'{distance_folder}/14_gamma_distance.csv', index=False)

"""
Part 3: Plot probability of exposure to deforestation based on gamma distance
"""

# Create x and y coordinates from cell_id
distance_agg['x'] = distance_agg['cell_id'].str.split('_').str[0].astype(float)
distance_agg['y'] = distance_agg['cell_id'].str.split('_').str[1].astype(float)

# Plot scatter plot
plt.scatter(distance_agg['x'], distance_agg['y'], c=distance_agg['probability'], cmap='hot', s=1)
plt.colorbar(label='Probability')
plt.savefig(f'{distance_folder}/14_probability_exposure.png', dpi=300, bbox_inches='tight')
