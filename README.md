# Map Tile Downloader

The Map Tile Downloader is a Flask-based web application designed to download map tiles from various sources. It allows users to select specific areas on a map, choose zoom levels, and download tiles for offline use. The application supports converting tiles to 8-bit color depth for compatibility with Meshtastic UI Maps and provides options to view and manage cached tiles.

## Features

- **Custom Area Downloads**: Draw polygons on the map to select specific areas for tile downloading.
- **World Basemap Downloads**: Download tiles for the entire world at zoom levels 0-7.
- **8-bit Conversion**: Option to convert downloaded tiles to 8-bit color depth for Meshtastic UI Maps.
- **Cache Management**: View and delete cached tiles for different map styles.
- **Progress Tracking**: Real-time progress bar showing downloaded, skipped, and failed tiles.
- **Configurable Map Sources**: Easily add or modify map sources via a JSON configuration file.

## Prerequisites

- Python 3.8 or higher
- A modern web browser (Chrome, Firefox, Edge, etc.)
- Git (for cloning the repository)

## Installation

1. Clone the Repository:
   
	git clone https://github.com/yourusername/map-tile-downloader.git
	cd map-tile-downloader
   
2. 	Install Dependencies:
    The application will automatically install required dependencies from requirements.txt on startup. However, you can manually install them using:

	pip install -r requirements.txt

3. Set Up Configuration:

   Ensure the config/map_sources.json file is present and correctly formatted. See the Configuration section below for an example.
   
   
##Configuration
The application uses a JSON configuration file (config/map_sources.json) to define available map sources. Each entry consists of a name and a URL template for the tiles.

Example map_sources.json:
	{
		"OpenStreetMap": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
		"OpenTopoMap": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
		"Stamen Terrain": "http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.png",
		"CartoDB Positron": "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png",
		"CartoDB Dark Matter": "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png"
	}

Adding a New Map Source: Simply add a new key-value pair to the JSON file with the map name and its tile URL template.


##Usage
1.	Run the Application:

		python src/TileDL.py
	
		The application will start a local server at http://localhost:5000.

2. 	Access the Web Interface:

		Open your web browser and navigate to http://localhost:5000.
		
3. 	Select Map Style:

		Choose a map style from the dropdown menu. The available options are loaded from map_sources.json.
4. 	Draw Polygons:
	
		Use the drawing tools to select areas on the map for which you want to download tiles.
		
5.	Set Zoom Levels:
	
		Specify the minimum and maximum zoom levels for the tiles you wish to download.

6.	Download Tiles:

		Click "Download Tiles" to start downloading tiles for the selected areas and zoom levels.
		Alternatively, click "Download World Basemap" to download tiles for the entire world at zoom levels 0-7.

7.	Monitor Progress:

		The progress bar will display the number of downloaded, skipped, and failed tiles.

8.	Manage Cache:

		Check "View cached tiles" to see outlines of cached tiles on the map.

		Use "Delete Cache" to remove cached tiles for the selected map style.


##Contributing

We welcome contributions to improve the Map Tile Downloader! To contribute:

-Fork the Repository: Create your own fork of the project.
-Create a Feature Branch: Work on your feature or bug fix in a separate branch.
-Submit a Pull Request: Once your changes are ready, submit a pull request to the main repository.
-Coding Standards: Follow PEP 8 for Python code and ensure your code is well-documented.
-Testing: Test your changes locally before submitting a pull request.

License

This project is licensed under the MIT License. See the  file for details.

Contact Information
For questions, suggestions, or support, please open an issue on the GitHub repository or contact k4mbd.ham@gmail.com

##Acknowledgements

Leaflet: For the interactive map interface.
Flask: For the web framework.
SocketIO: For real-time communication.
Mercantile: For tile calculations.
Shapely: For geometric operations.
Pillow: For image processing.

Special thanks to all contributors and the open-source community!
