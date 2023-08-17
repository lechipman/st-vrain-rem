# Watershed Project Repository

This is the repository for Julia and Lindsay's Earth Analytics Graduate Certificate Project (Spring-Summer 2023).

Find our completed blog post at watershed_project.html or run it yourself with the watershed_project_summer2023 jupyter notebook.

## Summary
This repositiory contains initial code, data, and instructions to demonstrate an expoloratory effort in using Digital Terrain Models (DTM's) saved in GitHub and running the REMMaker tool in the [RiverREM](https://github.com/OpenTopography/RiverREM) python library to generate a Relative Elevation Model (REM) over one of five study sites (Highway 93, Boulder, CO) for the purposes of floodplain mapping. The overall goal of the project is to create and compare REMs created from the RiverREM library and the [Colorado Hazard Mapping](https://coloradohazardmapping.com/) tool in ArcGIS. When complete, this project will provide an open, reporducible method to create REMs from existing DTMs. It will also compare the REMs created from DTMs generated from drone imagery with those created from LiDAR. This repository will provide information on the best ways to create REMs in terms of accuracy as well as effort, resources, etc.

## Background
A connected, functional floodplain retains water during periods of high flow and releases it back into the stream when flows are low. Reduced connectivity results in greater magnitude of flood events and vulnerability of surrounding ecosystems to drought. Climate change is causing higher peak flows and longer dry periods, potentially increasing the importance of maintaining and restoring floodplain connectivity, as restoration that increases floodplain connectivity could help reduce the magnitude of flood and drought events.  Therefore, understanding a river’s geomorphology is imperative to water resource  management and preparing for potential natural disasters.

REMs are DTMs that are normalized to the elevation of a channel. They can be useful to visualize fluvial landforms that may be hard to discern from an aerial image or DTM alone. Information provided by REMs can be used to plan and prioritize restoration projects that  improve watershed health. By analyzing REMs of target sites in the St. Vrain Basin in Boulder, CO, we hope to provide information on  floodplain connectivity for use in restoration work in the watershed as well as information on the pros and cons of each method (UAV- vs. LiDAR-derived imagery) for creating REMs. This information can be used to guide future monitoring workflows and budget.

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
  * For this assignment, we hosted preprocesed data on a github release. Data was from the [Watershed Center](https://watershed.center/)
  
## Workflow
 * Follow the environment installation instructions above.
 * Fork this repository and clone it to your local computer to run the code fully; NOTE: for the .html file to save properly, please create a subfolder in your home computer called 'earth-analytics' and fork the repository to this subfolder so the path to the local repository is as follows: home/earth-analytics/watershed-project 

 * Open watershed_project_Spring23.ipynb from the main directory ([watershed-project](https://github.com/lechipman/watershed-project)).
 * Run the jupyter notebook by selecting Run All.
 * The code will import the needed libraries, including RiverREM and plot_site_map.py, as well as the data (including the DTM and site coordinates hosted on github, see data access above) to run from start to finish.
 * The results show plots of the study sites and plots of a preliminary DTM and REM for one of the five study sites.
 * The code also downloads the notebook as a .html file.

## File Descriptions
* UAV_gps_coords.csv : the coordinates of the study sites
* plot_model.ipynb: jupyter notebook with code to plot the elevation models
* plot_mode.py : python file with code to plot the elevation models
* plot_site_map.ipynb: jupyter notebook with code to plot the study sites with two methods
* plot_site_map.py : python file with code to plot the study sites
* streamline_js_highway93.zip: shapefile of the streamline (not used in the current notebook version)
* watershed_project_summer23.ipynb : jupyter notebook with project code and current progress for summer semester, 2023
* watershed_project_summer23.html : blog post with project overview and current progress summer semester, 2023
* watershed_project_Spring23.ipynb : jupyter notebook with project code and current progress as of spring semester, 2023.

[![DOI](https://zenodo.org/badge/633148424.svg)](https://zenodo.org/badge/latestdoi/633148424)
