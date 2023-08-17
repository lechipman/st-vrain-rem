#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import directories
import os
import pathlib
import zipfile

import contextily as cx
import io
import folium
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import requests


# In[2]:


# Set working directory
working_dir = os.path.join(
    pathlib.Path.home(), 'earth-analytics', 'data', 'watershed-project')
if not os.path.exists(working_dir):
    print('{} does not exist. Creating...'.format(working_dir))
    os.makedirs(working_dir)

os.chdir(working_dir)


# In[3]:


# Define urls for plot data downloads
# Site coordinates (saved on github)
sites_url = ("https://raw.githubusercontent.com/lechipman/"
             "watershed-project/master/UAV_gps_coords.csv")
# Watershed boundary, USGS 
wbd_10_url = (
    "https://prd-tnm.s3.amazonaws.com/StagedProducts/"
    "Hydrography/WBD/HU2/Shape/WBD_10_HU2_Shape.zip")

# Boulder County streams data (University of Colorado, Boulder, GeoLibrary)
# https://geo.colorado.edu/catalog/47540-5ca23860d43267000b8c744e
stream_url = ("https://geo.colorado.edu/apps/geolibrary/"
              "datasets/STREAMSx4.zip")


# In[4]:


# Import the site coordinates for plotting (saved on github)
sites_download = requests.get(sites_url).content

# Read the downloaded content as a pandas dataframe
sites_df = pd.read_csv(io.StringIO(sites_download.decode('utf-8')))

# Select one location from each site to map
sites_short_df = sites_df.iloc[[0, 7, 17, 29, -1]]

# Create gdf of study sites
sites_gdf = gpd.GeoDataFrame(
    sites_short_df,
    geometry=gpd.points_from_xy(sites_short_df['lon'],
                                sites_short_df['lat']),
    crs='EPSG:4326')


# In[5]:


# Function to download data and unzip files
def download_data(data_url, data_name):
    """Downloads Data to a Local Directory
    
    Parameters
    ----------
    data_url: str
        Url to the desired data.
    data_name: str
        The name of the data.
        
    Returns
    ---------
    gdf : gpd.GeoDataFrame
        A geodataframe of requested data.

    """
    
    override_cache = False
    data_dir = data_name
    data_path = (os.path.join(data_dir, data_dir + '.zip'))
    
    # Cache data file
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

        if (not os.path.exists(data_path)) or override_cache:
            print('{} does not exist. Downloading...'.format(data_path))
            # Download full data file as zipfile
            response = requests.get(data_url)

            # Write in respose content using context manager
            with open(data_path, 'wb') as data_file:
                data_file.write(response.content)

            # Decompress zip file
            with zipfile.ZipFile(data_path, 'r') as data_zipfile:
                data_zipfile.extractall(data_dir)
    
    # For special case where data is downloaded in subfolders (WDB)
    # define new path to data and load as gdf
    if (data_name == 'water-boundary-dataset-hu10'):
        new_data_path = os.path.join(data_dir, 'Shape', 'WBDHU8.shp')
        temp_gdf = gpd.read_file(new_data_path)
        gdf = temp_gdf[temp_gdf.name.str.contains('Vrain')]
    
     # Otherwise load data from original path as gdf
    else:        
        gdf = gpd.read_file(data_path)

    # Set CRS of gdf to same as site points
    crs_gdf = gdf.to_crs(crs='EPSG:4326')
             
    return crs_gdf


# In[6]:


# Create gdf of st. vrain watershed boundary dataset
vrain_gdf = download_data(data_url = wbd_10_url, 
                        data_name = 'water-boundary-dataset-hu10')


# In[7]:


# Create gdf of Colorado streams
stream_gdf = download_data(data_url = stream_url, 
                        data_name = 'co_streams')

# Clip stream data to st vrain watershed boundary
stream_clipped_gdf = stream_gdf.clip(vrain_gdf)


# In[8]:


# Define dictionaries for mapping
site_symbol_dict = {
        'AV GCP1': '*',
        'HW93 GCP1': '*',
        'LEG1-GCP1': '*',
        'VV GCP1': '*',
        'HM': '*'
    }

site_name_dict = {
        'AV GCP1': 'Apple Valley North',
        'HW93 GCP1': 'Highway 93',
        'LEG1-GCP1': 'Legacy 1',
        'VV GCP1': 'Van Vleet',
        'HM': 'Hall Meadows'
    }


# In[9]:


# Plot Watershed and Streams - Method 1 (matplotlib)
def plot_sites():
    """Creates a map of study sites in the St. Vrain Watershed"""

    fig, ax = plt.subplots(1, 1, figsize=(8, 16))
    ax.set_title("Site Locations in the St. Vrain Watershed",
                 pad=20,
                 fontsize=16)

    stream_clipped_gdf.plot(ax=ax, color='blue')
    vrain_gdf.plot(ax=ax, facecolor='cyan', alpha=0.5)

    for i, gdf in sites_gdf.groupby('name'):
        gdf.plot(ax=ax,
                 marker=site_symbol_dict[i],
                 label=site_name_dict[i],
                 markersize=150,
                 legend=True,
                 zorder=3)

    ax.legend()
    ax.set_axis_off()
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
    cx.add_basemap(ax, crs=vrain_gdf.crs, zoom=10)


# In[10]:


# Plot Watershed and Streams - Method 2 (folium)
def plot_sites_folium():
    """Creates a map of study sites in the St. Vrain Watershed"""
    
    # style function
    stream_style_function = lambda x: {
        'color' :  'blue',
        'opacity' : 0.30,
        'weight' : 2}
    
    
    
    # Create map centered around Boulder
    m = folium.Map(
        location=[40.0150, -105.2705],
        tiles="Stamen Terrain",
        zoom_start=10
    )

    folium.GeoJson(
        vrain_gdf, 
        name="St. Vrain Watershed").add_to(m)
    
    folium.GeoJson(stream_clipped_gdf, name ="St. Vrain Streams", style_function = stream_style_function).add_to(m)

    for index, row in sites_short_df.groupby('name'):
        folium.Marker(
            location=[row.lat, row.lon],
            popup=site_name_dict[index],
            icon=folium.Icon(color="darkgreen")).add_to(m)
        
    return m

