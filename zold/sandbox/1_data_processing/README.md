# Visualization codes description


* `10_panel_pixel`

    * Title: Creating Pixel Panel
    * Description : Expand pixel dataset into yearly panel (2001–2024).
        Keep tree cover constant per pixel. Generate yearly
        forest loss indicator based on lossyear. 

    * input: 
        - Zambia_East_10s_030E_ForestBuffer_PixelPanel.dta

    * output:
        - Zambia_East_10s_030E_ForestBuffer_PixelPanel_panel
    

* `11_gamma_forest`

    * Title: Village distance to forest - gamma distribution
    * Description : This script analyzes the distribution of distances between villages and forests
    by fitting gamma distributions to distance data. It processes household-level
    data to estimate village-specific gamma distribution parameters.

    * input: 
        - Master Village ID list.xlsx: List of village IDs
        - CFP_HH.csv: Household-level data with distances to forest

    * output:
        - 11_ecdf_distance_forest_villages.png: ECDF plot of distances by village
        - 11_CFP_HH_forest_gamma_params.csv: Household data with fitted gamma parameters

* `12_gamma_crops`

    * Title: Village distance to plots - gamma distribution
    * Description : This script analyzes the distribution of distances between villages and forest plots
                 by fitting gamma distributions to distance data for each village. It processes household
                 survey data containing plot distances, creates empirical CDFs, and estimates gamma
                 distribution parameters.

    * input: 
        - Master Village ID list.xlsx: List of village IDs
        - CFP_HH.csv: Household survey data containing plot distances
    

    * output:
        - 12_ecdf_distance_plots_villages.png: Plot of empirical CDFs
        - 12_CFP_HH_plots_gamma_params.csv: Household data with fitted gamma parameters

