# Project Title: Driver-Pedestrian Interaction Analysis

## Project Overview

This project focuses on analyzing the interactions between drivers and pedestrians using various data sources and visualization techniques. The data includes body joint positions and specific pedestrian scenarios, which are visualized through Jupyter notebooks and generated videos.

## Directory Structure

The directory structure of the project is as follows:

```
Driver-Ped/
│
├── GeneratedVideos/
│
├── RawData/
│   ├── maps/
│   │   ├── Ped-104.jpeg
│   │   ├── Ped-105.jpeg
│   │   └── scene.jpeg
│   └── Pilot2/
│       └── csv/
│
├── body joints list.xlsx
│
├── Movement_Visualization_David.ipynb
│
├── Movement_Visualization_KK.ipynb
│
└── ReadME.md
```

## File Descriptions

- **GeneratedVideos/**: This directory contains HTML files with visualizations of pedestrian scenarios.
  
- **RawData/**: This directory contains raw data files used in the analysis.
  - **maps/**: Contains JPEG images of maps used in the analysis, more scenario-specific maps can be added later.
    - **Ped-104.jpeg**: Map image related to pedestrian scenario 104.
    - **Ped-105.jpeg**: Map image related to pedestrian scenario 105.
    - **scene.jpeg**: General scene map image used for visualization.
  - **Pilot2/**: Contains CSV files with raw data for the second pilot study.
    - **csv/**: Directory holding CSV files related to the pilot study.

- **body joints list.xlsx**: This Excel file contains the list of body joints used for visualizing pedestrian movements.

- **Movement_Visualization_David.ipynb**: Jupyter notebook for visualizing pedestrian movement data and generating 2D.mp4 videos, developed by David.

- **Movement_Visualization_KK.ipynb**: Jupyter notebook for visualizing pedestrian movement data and generating interactive 2D and 3D .html files, developed by KK.

- **ReadME.md**: This file, providing an overview of the project and the directory structure.


## Installation and Setup

1. Clone the repository:

   ```bash
   gh repo clone kzhuoxu/Driver_Ped_Interaction_Analysis
   ```

2. Download the data from this [Google Drive Link](https://drive.google.com/drive/folders/1yDvWvUWWHHmzT-3ZMJ18PT8RVv8kOYWc?usp=drive_link) and put the data in this directory.
   ```
   Driver-Ped/
   │
   ├── RawData/
   │   └── Pilot2/
   │       └── csv/
   ```
   

3. Navigate to the project directory:

   ```bash
   cd Driver-Ped
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preparation**: Ensure that the raw data is placed in the `RawData/` directory.
2. **Running Notebooks**: Open the Jupyter notebooks (`Movement_Visualization_David.ipynb` and `Movement_Visualization_KK.ipynb`) in Jupyter Lab or Jupyter Notebook.
3. **Visualization**: Execute the cells in the notebook `Movement_Visualization_KK.ipynb` to generate visualizations of the pedestrian movement data.
   - Driver-Ped 2D Animation: This section includes cells for generating 2D animations that illustrate the interaction between drivers and pedestrians.
   - Driver A: 3D Close-up Animation: This part of the notebook generates close-up 3D animations of Driver A, focusing on detailed movements and interactions.
   - Pedestrian B: 3D Close-up Animation: Similar to the Driver A section, this part generates close-up 3D animations of Pedestrian B, highlighting specific movements.
   - Run: This section contains the code to execute the full set of animations and visualizations. Running this will produce all the visual outputs as specified in the previous sections.
   - Testing: This section includes cells for testing the animations and visualizations before incorporating them into the "Run" section, to ensure they are correctly generated and aligned with the expected outcomes.
## Results

The results of the analysis are visualized in the form of plots and videos. These visualizations can be found in the `GeneratedVideos/` directory.

## Contributions

- **David**: Developed the `Movement_Visualization_David.ipynb` notebook.
- **KK**: Developed the `Movement_Visualization_KK.ipynb` notebook.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank all the contributors and data providers for their support in this project.

## Contact

For any queries or issues, please contact:

- KK: [zx325@cornell.edu](mailto:zx325@cornell.edu)

