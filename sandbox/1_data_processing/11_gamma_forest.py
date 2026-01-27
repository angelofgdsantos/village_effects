"""
Author: Angelo dos Santos   
Date: 2026-27-01
Title: Village distance to forest - gamma distribution

    Description: 
    This script analyzes the distribution of distances between villages and forests
    by fitting gamma distributions to distance data. It processes household-level
    data to estimate village-specific gamma distribution parameters.

    Usage: 
    Run the script to:
    1. Load and clean household distance data
    2. Generate ECDF plots of distances by village
    3. Fit gamma distributions to each village's distance data
    4. Save the estimated parameters merged with household data

    Parts:
        1. Load and clean village and household distance data
        2. Plot empirical cumulative distribution functions by village
        3. Fit gamma distributions and extract parameters for each village
        4. Merge parameters back to household data and save results

    Inputs:
    - Master Village ID list.xlsx: List of village IDs
    - CFP_HH.csv: Household-level data with distances to forest
    
    Outputs:
    - 11_ecdf_distance_forest_villages.png: ECDF plot of distances by village
    - 11_CFP_HH_forest_gamma_params.csv: Household data with fitted gamma parameters
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
# distance_cols = ['fordistance_1', 'fordistance_2', 'fordistance_3', 'fordistance_4', 'fordistance_5']
distance_cols = ['fordistance_1']

households = households[['vilid'] + distance_cols]

# Drop if distance is -98
households = households[households['fordistance_1'] != -98]

# Replace -98 with NaN in distance columns  
# households[distance_cols] = households[distance_cols].replace(-98, np.nan)

"""
Part 2: Plot ECDF of distance to forest for all villages
"""

# Plot ECDF of distance to forest for a single village
ax = sns.ecdfplot(data=households, x='fordistance_1', hue='vilid', palette='viridis')
ax.get_legend().remove()

# X label
ax.set_xlabel('Distance to Forest (km)')

# Y label
ax.set_ylabel('Empirical CDF')

# Save figure
ax.figure.savefig(f'{outputs_figures}11_ecdf_distance_forest_villages.png', dpi=300)

"""
Part 3: Fit gamma distribution to distance to forest for each village
"""

gamma_params_list = []

for vilid, group in households.groupby('vilid'):
    
    # 1. Drop NaNs and zeros (Gamma is only defined for x > 0)
    data = group['fordistance_1'].dropna()
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
households_final.to_csv(f'{output_data}11_CFP_HH_forest_gamma_params.csv', index=False)

print("Gamma distribution fitting complete. Parameters saved and merged.")