<div align="center"> <h1> POLLUTION MONITORING WITH SENTINEL-5P </h1> </div>
<div align="center"> <h2> Case Study: Paris 2019 vs. 2020 </h2> </div>

&ensp;&ensp; Governments and decisin-makers rely heavily on satellite data and computer models to show how pollution accumulates and how it is carried in the air so that they can develop appropriate mitigation strategies.One of the missions, known as a Sentinel-5p, provides timely data on a multitude of trace gases(CO, NO2, S02, O3, aerosols, etc.)

In this study, a comparison of air pollution between the years was made by comparing the 2019 and 2020 images of France. Analysis carried out based on Sentinel-5 products, delivered to users as a netCDF files, to map NO2 concentration over our study area in France.

The exercise is divided in the following sections:
<br>&ensp;1.&ensp;Python Modules
<br>&ensp;2.&ensp;Explore Sentinel-5p Data
<br>&ensp;&ensp;&ensp;&ensp;2.1 Access Groups
<br>&ensp;&ensp;&ensp;&ensp;2.2 Access variable
<br>&ensp;&ensp;&ensp;&ensp;2.3 Plot variable
<br>&ensp;&ensp;&ensp;&ensp;2.4 Filter variable

<h3> 1- PYTHON MODULES </h3>
It is the section where the required libraries are loaded and run for viewing metadata, extracting data value from metadata, filtering and improving the data obtained from metadata, and displaying the results.

<i>(Used libraries: numpy, xarray, cartopy, termcolor, matplotlib)</i>

<h3> 2- EXPLORE SENTINEL-5P DATA </h3>
<h4> 2.1- Access Groups </h3>
With in netCDF files, different groups are used to organise the data and make it easier to find what you are looking for. Two groups: PRODUCT and METADATA, both of them contain sub-groups.

<br><b>PRODUCT</b>: The variables in this group will answer the questions what, when, where and how well.

<b>METADATA</b>: This is a group to collect metadata items, such as the items that appear in the header file and items. The metadata is stored as attributes, while grouping attributes that belong to a specific standart will be done by using sub-groups.

In this study, xarray library was used to perform basic and advanced analysis. Xarray introduces labels in the form of dimensions, coordinates and attributes on top of raw NumPy-like array, which allows for a more intuitive, more concise, and less error-prone developer experience.

<b>In the Access Groups section was carried out with these parts:</b>
<br>&ensp;- Access the Global Attributes
<br>&ensp;- Access the METADATA group
<br>&ensp;- Access the METADATA group

<h4> 2.2- Access Variable </h3>
The most important question is where can we find the actual NO2 measurement? When check the Sentinel-5p Level 2 NO2 product User Manuel, it will be learned. This information can be found in the <i>'nitrogendioxied_tropospheric_column'</i> variable inside the PRODUCT group. So, we can make use of the key properties available. In this section, group products metadata is shown and the relevant NO2 data can be seen easily.

<h4> 2.3- Plot Variable </h3>
In the next step, the unit used to represent the measure was converted from <b><i>"mol/m2"</i></b> to <b><i>"molecules/cm2"</i></b> using the <b><i>"multiplication_factor_to_convert_to_molecules_percm2"</i></b> attribute in the PRODUCT group. 

<br><i><b>Tip:</b> The quantities in Sentinel 5 precursor files are given in SI units. For an integrated column value this means that the unit is mol/m2. Traditionally, the unit for an integrated column is molecules/cm2.</i>

<h4> 2.4- Filter Variable </h3>

With the overview of the data completed, our processing started using the quality flag included on the Sentinel-5p Level 2 product. The quality of the individual observations depends on many factors, <u>including cloud cover</u>, <u>surface albedo</u>; <u>presence of snow-ice</u>, <u>saturation</u>, <u>geometry</u> etc. 

These aspects are taken into account in the definition of the <i>"quality assurance value (qa_value)"</i>, available for each individual observation, which provides the users with an easy filter to remove less accurate observations. The <i>"qa_value"</i> is a continuous variable, ranging from 0(error) to 1(well).


