# Datasets documentation

* Zambia_East_10s_030E_ForestBuffer_PixelPanel

    - Description : A pixel-level panel dataset for pixels 5 km around treated villages in Eastern Zambia or 5 km from settlements 5 km or less from treated villages with tree cover and tree cover loss data from Hansen et al. (2013).
    - Code source : 
    - Main columns : 

        - x : Longitude
        - y : Latitude
        - treecover : Tree cover percentage
        - lossyear : year of tree cover loss, 0 otherwise


* Zambia_East_10s_030E_ForestBuffer_Cover

    - Description : A pixel-level dataset for pixels 5 km around treated villages in Eastern Zambia or 5 km from settlements 5 km or less from treated villages with tree cover data from Hansen et al. (2013).
    - Code source : 
    - Main columns : 

        - x : Longitude
        - y : Latitude
        - treecover : Tree cover percentage


* Zambia_East_10s_030E_ForestBuffer_LossYear

    - Description : A pixel-level dataset for pixels 5 km around treated villages in Eastern Zambia or 5 km from settlements 5 km or less from treated villages with tree cover loss data from Hansen et al. (2013).
    - Code source : 
    - Main columns : 

        - x : Longitude
        - y : Latitude
        - lossyear : year of tree cover loss, 0 otherwise

* 10_pixel_panel.dta

    - Description : A pixel-level panel dataset for pixels 5 km around treated villages in Eastern Zambia or 5 km from settlements 5 km or less from treated villages with tree cover loss data from Hansen et al. (2013).
    - Code source : 10_panel_pixel.py
    - Main columns : 

        - pixel_id : Unique pixel identifier
        - year : Year of observation
        - treecover : Tree cover percentage
        - lossyear : year of tree cover loss, 0 otherwise
        - loss : Binary indicator for tree cover loss in that year, missing if year after the year of loss.
        
