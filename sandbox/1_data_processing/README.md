# Visualization codes description


* `10_gta_processing`

    * Title: Processing GTA data 
    * Description : This script processes the GTA dataset for Acre state, extracting relevant information such as year, month, and day from the emission date column, and counting the number of digits in CPF/CNPJ columns to differentiate between individual and corporate entities. It also integrates property information from various datasets including shapefiles and CAR data.
    * input: 
        - GTA dataset: RELATORIO_GTA_2012_2019.xlsx

    * output:
        - Processed GTA data: p_10_gta_processed.csv
    


* `11_process_data_receita_federal`

    * Title: Processing receita federal data (CAFIR) and SNCR
    * Description : This scripts merge CAFIR and SNCR
    * input: 
        - Input file: K34313UF.D50801.AC01.csv (fixed-width format) from Receita federal
        - Input file: Imoveis_AC_01_08_2025.csv from SNCR

    * output:
        - Output file: 11_receita_federal_cafir_acre.csv (cleaned CSV format)
        - Output file: 11_sncr_cafir_acre.csv (cleaned CSV format)    
