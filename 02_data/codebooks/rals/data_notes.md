# My Data notes on RALS

- Village infomation: 

    - In 2015 in the file "id.sav" there is a a variable (vil15) with 3516 unique values. Check the number of settlemenyd in grid3

- Chief information:

    - 

## 2012

## 2015

### id.sav

- 'cluster': 'Cluster',
- 'hh': 'Household number',
- 'category': 'Farmer Category',
- 'vil15': 'New village name',
- 'resp_mem': 'member number of the respondent from old member table',
- 'resp15': 'Respondent name',
- 's_dd_new': 'South Coordinate in decimal degrees',
- 'e_dd_new': 'East Coordinate in decimal degrees',
- 'rstatus': 'Response status',
- 'consent': 'Respondent explained the consent form',
- 'encode': 'Enumerator code',
- 'spcode': 'Supervisor code',
- 'qccode': 'Quality controller code',
- 'pstatus': None,
- 'prov': 'Province',
- 'dist': 'District',
- 'const': 'Constituency',
- 'ward': 'Ward',
- 'region': 'Region',
- 'csa': 'Census Supervisory Area',
- 'sea': 'Standard Enumeration Area'

### household.sav

This data has information on HH questionS, these are some questions I selected and are related to my quesiton.

- 'have_fields': 'Does this household have any fields?'
- 'hh42': 'Does the household get access to information about agricultural commodity prices?'
- 'hh43': "What is the household's main source of agricultural commodity price information?"
- 'hh09a': 'In your perception, do village headmen/authorities still have unallocated arable land that could be given to households in this area?' 
- 'hh09b': 'If yes to 2.9.3 If your hh wanted more land, could some of this unallocated land be allocated to this household for cropping purposes?'
- 'hh10a': 'Is it possible to change the tenure status of customary land in this village (i.e. to convert customary land into titled property)?'
- 'hh10b': 'Is it possible to buy or sell customary land in this village, without first changing it to titled land?'
- 'hh50a': 'Is the headman in this village/locality related to the head of the household?' 
- 'hh51a': 'Is the chief of this village/locality related to the head of the household?'
- 'hh53a': 'Tribe of the current head'


### inherit.sav

This data set has information on inhererited cattle and land for each household 

- 'cluster': 'Cluster'
- 'hh': 'Household number'
- 'inherit': 'Type of inheritance received'
- 'ih01': 'Year in which inheritance was received'
- 'ih02': 'What was the area of land or number of cattle that was received? (Quantity)'
- 'ih03': 'Unit of quantity received'
- 'convert': 'Conversion value to hectares'
- 'hect': 'Hectares inherited'
- 'prov': 'Province'
- 'dist': 'District'
- 'pstatus': 'Panel Status: Panel or New Household'

### wages.sav

This file has infomration on the wage source of the households, the strucytre of the tha is such that every household answers the same set of questions. I need to filter using anywork == 1, meaning the HH worked on that. 

### labour.sav

This file informs the type of agriculture labour activities done by the HH.

- 'labour': 'Agricultural labour activities'
- 'lbr01': 'Did the household hire labour for this activity during the 2013/14 agricultural season?'
- 'lbr02': 'What was the total cost to hire labour for this activity for the 2013/14 agricultural season?'
 
### wild.sav

This file has information about wild product collection and specific question about charcoal

- 'wildprod': 'Wild products and charcoal'
- 'wd01': 'Was any of this product collected for home consumption or use between 1st May 2014 and 30th April 2015?'
- 'wd01a': 'From the homestead, how far is it to the primary source of this product? (km)'
- 'wd01b': 'Reason charcoal/firewood not collected'
- 'wd02': 'Who provided most of the labour for this activity?'
- 'wd03': 'Between 1st May 2014 and 31st October 2014, what was the total value consumed or used by the HH from own collection? (ZMW)'
- 'wd04': 'Between 1st November 2014 and 30th April 2015, what was the total value consumed or used by the HH from
 own collection? (ZMW)'

### soil_land_manage.sav

This module have some infomration on land management that can be interesting for me

- slm00': 'Soil and Land Management Practices',
- 'slm01': 'Did this HH implement this activity during the 2013/14 agricultural season?',
- 'slm02': 'In which year did this HH begin implementing this practice?',
- 'slm03': 'Did this HH continue to implement this practice in the 2014/15 current agricultural season?',
- 'slm04': 'Did this HH ever practice this in the past (before the 2013/14 agricultural season)?',
- 'slm05': 'Up through the 2013/14 agricultural season, what is the main reason why this HH never used this activity?',
- 'slm06a': 'First crop',
- 'slm06b': 'Second crop',
- 'slm06c': 'Third crop',
- 'slm06d': 'Fourth crop',
- 'slm06e': 'Fifth crop',
- 'slm06f': 'Sixth crop',
- 'slm07': 'What is the main reason why this HH abandoned this activity?',
- 'slm05_oth': 'Text Entry',XX
- 'slm07_oth': 'Text Entry',

### salwage.sav

This informs about wage and income from the family

### distance_agser.sav

This informs about distance to agriculture services

### field.sav

This informs a lot of thing about the field, I think the distance to field is something very useful for me. There is also infomration of land ternure and who sets the rules for using the land.

- 'cluster': 'Cluster',
- 'hh': 'Household number',
- 'field': 'All fields owned and used by the household',
- 'field_name': 'Unique plot name',
- 'f01': 'Land use of the plot',
- 'popwgt': 'Population weight',
- 'panwgt': 'Panel weight',
- 'f02': 'Area of field',
- 'f03': 'Unit of area for this field',
- 'hect': 'Hectares',
- 'f03a': 'What is the distance of this field from the homestead?',
- 'f03b': 'Unit of distance to field',
- 'dist_plot': 'Distance to plot',
- 'f04': 'Who primarily decided how to use this field?',
- 'f04a': 'Member number of person making decision on field',
- 'da02': 'Gender of decision maker',
- 'f05': 'Tenure status of this field',
- 'f06': 'How did this household acquire this field?',
- 'f07': 'From whom did this household obtain this field?',
- 'f08': 'Was this field in a wetland / dambo area?',
- 'f09': 'Did this hh irrigate this field?',
- 'f10': 'Is this field prone to soil erosion and/or flash flooding?',
- 'f11': 'What, if anything, did the hh do to prevent soil erosion and/or flash flooding in this field?',
- 'f13': 'What main crop or use did the hh put this field to in the 2012/13 agricultural season(2 seasons ago)?',
- 'f14': 'How was the crop/field residue from this field from the 2012/13 agricultural season (2 seasons ago) mainly used or disposed of?',
- 'f15': 'What main crop or use did the hh put this field to this agricultural season (2014/15)?',
- 'f12': 'Are there any trees/shrubs growing in this field?',
- 'prov': 'Province',
- 'dist': 'District',
-  'pstatus': 'Panel Status: Panel or New Household',
- 'convert': 'Conversion value to hectares',
- 'category': 'Farmer Category'
