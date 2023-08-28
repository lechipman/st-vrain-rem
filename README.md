# St-Vrain-REM Repository

This is the repository for Julia Soczak's and Lindsay Chipman's Earth Analytics Graduate Certificate Project (Spring-Summer 2023).

Find our completed blog post at 'taking-the-low-road-blog.html' or run it yourself with the jupyter notebook, 'taking-the-low-road-blog.ipynb'.

## Summary
This repositiory contains the code, data, and instructions to demonstrate an expoloratory effort in using Relative Elevation Models (REMs) to investigate floodplain connectivity at five study sites in the St. Vrain Basin. The REMs were created from Digital Elevation Models (DTMs) generated with two different data sources (drone or Unmanned Aerial Vehicles [UAV] and Light Detection and Ranging [LiDAR] data) and two different tools (the [Colorado Hazard Mapping](https://coloradohazardmapping.com/) tool in ArcGIS and the REMMaker tool [RiverREM](https://github.com/OpenTopography/RiverREM) python library).

The overall goal of the project was to create and compare REMs created with the two different data sources and tools and to use the REMs to visualize how connected floodplains mitigate the impacts of heavy flooding.

## Background
A floodplain is the area adjacent to a stream that becomes inundated with water when a flood occurs. This space allows the flood to spread out and release energy and suspended objects such as sediment, logs, and debris. By reducing the flow of water down the stream corridor, floodplains effectively mitigate destruction to buildings and other infrastructure downstream (FISRWG 1998). BUT this can only happen if the floodplain is "available" to the stream i.e., if the area around the stream is low enough to be inundated when floodwaters occur. If a floodplain is situated above the highest flow of water, it will not be accessible by the stream - we call this a disconnected floodplain (American Rivers 2016).

REMs are DTMs that are normalized to the elevation of a channel. They can be useful to visualize fluvial landforms that may be hard to discern from an aerial image or DTM alone. Information provided by REMs can be used to plan and prioritize restoration projects that improve watershed health. By analyzing REMs of target sites in the St. Vrain Basin in Boulder, CO, we hope to provide information on floodplain connectivity for use in restoration work in the watershed as well as information on the pros and cons of each method (UAV- vs. LiDAR-derived imagery) for creating REMs. This information can be used to guide future monitoring workflows and budget.

## Collaborators and Acknowledgements
Julia Sobczak, Lindsay Chipman, Matthew Bitters with the [Watershed Center](https://watershed.center/), and University of Colorado [Earth Lab](https://earthlab.colorado.edu/)

## Environment Requirements
How to install your environment
  * Start with [instructions for installing the ea-python environment](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/)
  *  Install [OpenTopography RiverREM package](https://github.com/OpenTopography/RiverREM)

  ```bash
  conda install -c conda-forge riverrem
  ```

## Data Access
  * We hosted our preprocesed data on a github release and on zenodo. All the UAV data was from the [Watershed Center](https://watershed.center/), and the LiDAR data was obtained from [Colorado Hazard Mapping](https://coloradohazardmapping.com/).
  
## Workflow
 * Follow the environment installation instructions above.
 * Fork this repository and clone it to your local computer to run the code fully; NOTE: for the .html file to save properly, please create a subfolder in your home directory called 'earth-analytics' and fork the repository to this subfolder so the path to the local repository is as follows: home/earth-analytics/st-vrain-rem 
 * Open the jupyter notebook 'taking-the-low-road-blog.ipynb from the main directory [st-vrain-rem](https://github.com/JuliaSobczak/st-vrain-rem/tree/main).
 * Run the jupyter notebook by selecting Run All.
 * The code will import the needed libraries, including RiverREM, plot_site_map.py, and load_model.py, as well as the images and data to run from start to finish. The UAV DTMs and REMs and predowloaded LiDAR data are hosted on [zenodo](https://zenodo.org/record/8218054).
 * The results show the high resolution UAV REMs for each of the five sites. We also create raster plots and histograms for UAV and LiDAR REMs at two sites that contrast in terms of connectivity and complexity. Finally, the notebook runs a flood simulation at the two sites to visualize how connected and disconnected floodplains compare in their ability to store water during flooding.
 * The code also downloads the notebook as a .html file.


## File Descriptions
* plot_site_map.py : python file with code to plot the study sites
* load_model.py : python file with code to load the data, plot the elevation models and histograms, and create parameters to run the flood simulation
* taking-the-low-road-blog.ipynb : jupyter notebook with project code to create all the visualizations, run the flood simulation, and export the content as an html file. 
* taking-the-low-road-blog.html : blog post with our final project results.
* media: directory that contains images displayed in the final notebook and blog post

[![DOI](https://zenodo.org/badge/679505515.svg)](https://zenodo.org/badge/latestdoi/679505515)

