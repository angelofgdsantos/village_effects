"""
Author: Angelo dos Santos   
Date: 2026-27-01
Title: Village distance to plots - gamma distribution

    Description: This script analyzes the distribution of distances between villages and forest plots
                 by fitting gamma distributions to distance data for each village. It processes household
                 survey data containing plot distances, creates empirical CDFs, and estimates gamma
                 distribution parameters.

    Usage: Run the script to process household distance data, generate visualizations, and fit gamma
           distributions. The results are saved as new data files and plots.

    Parts:
        1. Load and clean village and household distance data
        2. Generate empirical CDF plots of distances by village 
        3. Fit gamma distributions to distance data for each village
        4. Merge gamma parameters back to household data and save results

    Inputs:
        - Master Village ID list.xlsx: List of village IDs
        - CFP_HH.csv: Household survey data containing plot distances
    
    Outputs:
        - 12_ecdf_distance_plots_villages.png: Plot of empirical CDFs
        - 12_CFP_HH_plots_gamma_params.csv: Household data with fitted gamma parameters

"""

"""
Packages
"""

import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
from scipy.stats import gamma

"""
Globals
"""

input_data = '/Users/angelosantos/UH-ECON Dropbox/Angelo Santos/village_effects/data/input/'
output_data = '/Users/angelosantos/UH-ECON Dropbox/Angelo Santos/village_effects/data/output/'
outputs_figures = '/Users/angelosantos/UH-ECON Dropbox/Angelo Santos/village_effects/outputs/figures/'

"""
Functions
"""

"""
Part 1: Call village data
"""

# Village ids
village_ids = pd.read_excel(f'{input_data}Master Village ID list.xlsx')

# Household data
households = pd.read_csv(f'{input_data}CFP_HH.csv')

# Select relevant columns
distance_cols = ['distance_1', 'distance_2', 'distance_3', 'distance_4', 'distance_5']
distance_cols = ['distance_1']

# Distance units : 1 meters, 2 kilometers
distance_units = ['distunit_1']

# Transform to kilometers if in meters and greater than 1 meter
households.loc[(households['distunit_1'] == 1) & (households['distance_1'] > 1), distance_cols] = households[distance_cols]/1000

# Select relevant columns
households = households[['vilid'] + distance_cols]

# Drop if distance is -98
households = households[households['distance_1'] > 0]

# Drop distances below 80 km 
households = households[households['distance_1'] < 100]

# Replace -98 with NaN in distance columns  
# households[distance_cols] = households[distance_cols].replace(-98, np.nan)

"""
Part 2: Plot ECDF of distance to forest for all villages
"""

# Plot ECDF of distance to forest for a single village
ax = sns.ecdfplot(data=households, x='distance_1', hue='vilid', palette='viridis')
ax.get_legend().remove()

# X label
ax.set_xlabel('Distance to Forest (km)')

# Y label
ax.set_ylabel('Empirical CDF')

# Save figure
ax.figure.savefig(f'{outputs_figures}12_ecdf_distance_plots_villages.png', dpi=300)

"""
Part 3: Fit gamma distribution to distance to forest for each village
"""

gamma_params_list = []

for vilid, group in households.groupby('vilid'):
    
    # 1. Drop NaNs and zeros (Gamma is only defined for x > 0)
    data = group['distance_1'].dropna()
    data = data[data > 0] 
    
    # 2. Check for sufficient observations and variance
    # If all values are the same (e.g., everyone is 1km away), the fit will fail
    if len(data) > 1 and data.std() > 0:
        try:
            # shape (alpha), location (fixed to 0), and scale (beta)
            shape, loc, scale = gamma.fit(data, floc=0)
            
            gamma_params_list.append({
                'vilid': vilid,
                'gamma_shape': shape,
                'gamma_scale': scale,
                'obs_count': len(data),
                'mean_dist': data.mean()
            })
        except (ValueError, RuntimeError) as e:
            print(f"Skipping village {vilid} due to fit error: {e}")
    else:
        print(f"Skipping village {vilid}: Insufficient data or zero variance.")

# Create a DataFrame with the estimated parameters
village_gamma_params = pd.DataFrame(gamma_params_list)

"""
Part 4: Merge parameters back to households and save
"""

# Merge the village-level parameters back to the household data
# This allows you to use shape/scale as village-level controls in regressions
households_final = households.merge(village_gamma_params, on='vilid', how='left')

# Save the updated household dataset
households_final.to_csv(f'{output_data}12_CFP_HH_plots_gamma_params.csv', index=False)

print("Gamma distribution fitting complete. Parameters saved and merged.")