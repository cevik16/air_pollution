# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 04:00:29 2021

@author: cevik
"""

 #POLLUTION MONITORING WITH SENTINEL-5P
 #Case Study: Paris 2019 vs. 2020 
 
from matplotlib import pyplot as plt # Visualization
from termcolor import colored
import matplotlib.colors as colors # colors for visualization
import xarray as xr # Process netCDF S-5p data
import numpy as np # Data manipulation
import cartopy # visualization
import cartopy.crs as ccrs
import matplotlib.gridspec as gridspec # create subplot
from glob import iglob # data access in file manager
from os.path import join
from functools import reduce # strinf manipulation
import cartopy.feature as cf

########### IMAGE DATA - 2019 ##########

# Look for NO2 products in 2019 Image
product_path_2019 = "Data/2019/"
input_files_OFFL_2019= sorted(list(iglob(join(product_path_2019, '**', '*OFFL*NO2*.nc'), recursive=True)))
print(colored('NO2 OFFL products detected:','blue'), len(input_files_OFFL_2019))

# Select Level2 NO2 product to be explored in 2019 Image
s5p_file_2019 = input_files_OFFL_2019[0]
print(colored('Product selected for analysis:','blue'), s5p_file_2019)

# Open product - GLOBAL ATTRIBUTES (2019 Image)
with xr.open_dataset(s5p_file_2019) as s5p_img_GA_2019:
    print(colored("Global attributes of product:\n" , "blue"), s5p_img_GA_2019)

# Open product - GROUP METADATA/GRANULE_DESCRIPTION (2019 Image)
with xr.open_dataset(s5p_file_2019, group='METADATA/GRANULE_DESCRIPTION') as s5p_img_MT_2019:
    print(colored("\nMETADATA/GRANULE_DESCRIPTION Group:\n" , "blue"), s5p_img_GA_2019)

# Open product - GROUP PRODUCT (2019 Image)
with xr.open_dataset(s5p_file_2019, group='PRODUCT') as s5p_img_PRD_2019:
    print(colored("\nPRODUCT Group:\n" , "blue"), s5p_img_GA_2019)

########### IMAGE DATA - 2020 ##########

# Look for NO2 products in 2020 Image
product_path_2020 = "Data/2020/"
input_files_OFFL_2020= sorted(list(iglob(join(product_path_2020, '**', '*OFFL*NO2*.nc'), recursive=True)))
print(colored('NO2 OFFL products detected:','blue'), len(input_files_OFFL_2020))

# Select Level2 NO2 product to be explored in 2020 Image
s5p_file_2020 = input_files_OFFL_2020[0]
print(colored('Product selected for analysis:','blue'), s5p_file_2020)

# Open product - GLOBAL ATTRIBUTES (2020 Image)
with xr.open_dataset(s5p_file_2020) as s5p_img_GA_2020:
    print(colored("Global attributes of product:\n" , "blue"), s5p_img_GA_2020)

# Open product - GROUP METADATA/GRANULE_DESCRIPTION (2020 Image)
with xr.open_dataset(s5p_file_2020, group='METADATA/GRANULE_DESCRIPTION') as s5p_img_MT_2020:
    print(colored("\nMETADATA/GRANULE_DESCRIPTION Group:\n" , "blue"), s5p_img_GA_2020)

# Open product - GROUP PRODUCT (2020 Image)
with xr.open_dataset(s5p_file_2020, group='PRODUCT') as s5p_img_PRD_2020:
    print(colored("\nPRODUCT Group:\n" , "blue"), s5p_img_GA_2020)

########### DETERMINE NO2 VARIABLE ##########

no2_2019 = s5p_img_PRD_2019['nitrogendioxide_tropospheric_column']
print(colored('Dimension: names for each axis (e.g., ("x", "y", "z"):','blue'), no2_2019.dims)
print(colored('\nCoordinates: dict-like container of arrays that label each point: ', 'blue'), no2_2019.coords)
print(colored('\nAttributes: dict to hold arbitrary metadat (attributes):\n', 'blue'), no2_2019.attrs)
print(colored('\Values: a numpy.ndarray holding the array values:\n','blue'), no2_2019.values)

no2_2020 = s5p_img_PRD_2020['nitrogendioxide_tropospheric_column']
print(colored('Dimension: names for each axis (e.g., ("x", "y", "z"):','blue'), no2_2020.dims)
print(colored('\nCoordinates: dict-like container of arrays that label each point: ', 'blue'), no2_2020.coords)
print(colored('\nAttributes: dict to hold arbitrary metadat (attributes):\n', 'blue'), no2_2020.attrs)
print(colored('\Values: a numpy.ndarray holding the array values:\n','blue'), no2_2020.values)

########### CONVERTING UNIT ##########

# Convert values to molecules/cm2 (2019 Image)
no2_2019 = no2_2019 * no2_2019.multiplication_factor_to_convert_to_molecules_percm2

# Convert values to molecules/cm2 (2020 Image)
no2_2020 = no2_2020 * no2_2020.multiplication_factor_to_convert_to_molecules_percm2

########### VISUALIZATION - 2019 ##########

plt.figure(figsize=(20,5.5))
ax = plt.axes(projection=ccrs.Mercator())
no2_2019[0].plot.pcolormesh(ax=ax, x='longitude', y='latitude', add_colorbar=True, cmap='magma_r', transform=ccrs.PlateCarree(), vmin=0)

ax.set_title('S-5P L2 NO$_2$ (2019) | Unfiltered Quality')
ax.coastlines('10m')
ax.set_global()
ax.stock_img()
ax.gridlines()
ax.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Map
ax.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

plt.savefig('Outputs/2019_NO2_unfiltered.png', bbox_inches='tight', dpi=300)

########### VISUALIZATION - 2020 ##########

plt.figure(figsize=(20,5.5))
ax = plt.axes(projection=ccrs.Mercator())
no2_2020[0].plot.pcolormesh(ax=ax, x='longitude', y='latitude', add_colorbar=True, cmap='magma_r', transform=ccrs.PlateCarree(), vmin=0)

ax.set_title('S-5P L2 NO$_2$ (2020) | Unfiltered Quality')
ax.coastlines('10m')
ax.set_global()
ax.stock_img()
ax.gridlines()
ax.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Map
ax.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

plt.savefig('Outputs/2020_NO2_unfiltered.png', bbox_inches='tight', dpi=300)

########### QUALITY FILTERING - 2019 ##########

plt.figure(figsize=(20, 5.5))

#Plot qa_value (2019 Image)
ax1 = plt.subplot(121, projection=ccrs.Mercator())
s5p_img_PRD_2019['qa_value'][0].plot.pcolormesh(ax=ax1, x='longitude', y='latitude', add_colorbar=True, cmap='Spectral', transform=ccrs.PlateCarree())
ax1.set_title('S-5p L2 NO$_2$ (2019) | Quality Assesment')
ax1.add_feature(cartopy.feature.LAND, edgecolor='black')
ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.RIVERS)
ax1.coastlines('10m')
ax1.gridlines()
ax1.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Maps (2019 Image)
ax1.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax1.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

# Save figure to file (2019 Image)
plt.savefig('Outputs/2019_Quality_Assesment.png', bbox_inches='tight', dpi=300)

########### QUALITY FILTERING - 2020 ##########
plt.figure(figsize=(20, 5.5))

#Plot qa_value (2020 Image)
ax1 = plt.subplot(121, projection=ccrs.Mercator())
s5p_img_PRD_2020['qa_value'][0].plot.pcolormesh(ax=ax1, x='longitude', y='latitude', add_colorbar=True, cmap='Spectral', transform=ccrs.PlateCarree())
ax1.set_title('S-5p L2 NO$_2$ (2020) | Quality Assesment')
ax1.add_feature(cartopy.feature.LAND, edgecolor='black')
ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.RIVERS)
ax1.coastlines('10m')
ax1.gridlines()
ax1.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Maps (2020 Image)
ax1.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax1.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

# Save figure to file (2020 Image)
plt.savefig('Outputs/2020_Quality_Assesment.png', bbox_inches='tight', dpi=300)

########### FINAL PLOTTING ##########

# Plotting
plt.figure(figsize=(20, 7.5))

## For 2019 Image ##

# Quality Filtering 
no2_filter_2019 = no2_2019.where(s5p_img_PRD_2019['qa_value'] > 0.75, drop=True)

# Plot masked NO2 data
ax1 = plt.subplot(122, projection=ccrs.Mercator())
no2_filter_2019[0].plot.pcolormesh(ax=ax1, x='longitude', y='latitude', add_colorbar=True, cmap='magma_r', transform=ccrs.PlateCarree(), vmin=0)
ax1.set_title('S-5p L2 NO$_2$ (2019) | Filtered Quality (qa_value > 0.75)')
ax1.add_feature(cartopy.feature.RIVERS)
ax1.coastlines('10m')
ax1.stock_img()
ax1.gridlines()
ax1.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Map
ax1.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax1.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

## For 2020 Image ##

# Quality Filtering 
no2_filter_2020 = no2_2020.where(s5p_img_PRD_2020['qa_value'] > 0.75, drop=True)

# Plot masked NO2 data
ax2 = plt.subplot(121, projection=ccrs.Mercator())
no2_filter_2020[0].plot.pcolormesh(ax=ax2, x='longitude', y='latitude', add_colorbar=True, cmap='magma_r', transform=ccrs.PlateCarree(), vmin=0)
ax2.set_title('S-5p L2 NO$_2$ (2020) | Filtered Quality (qa_value > 0.75)')
ax2.add_feature(cartopy.feature.RIVERS)
ax2.coastlines('10m')
ax2.stock_img()
ax2.gridlines()
ax2.set_extent([-3.62, 12.25, 44.00, 51.60])

# Add France to Map
ax2.plot(3.7, 46.8, 'bo', markersize=10, transform=ccrs.PlateCarree())
ax2.text(3.1, 47, 'FRANCE', transform=ccrs.Geodetic())

# Save figure to file
plt.savefig('Outputs/Comparing_results.png', bbox_inches='tight', dpi=300)

