# Map Tile Downloader

A Flask-based web application to download map tiles from various sources, with options for world basemaps, 8-bit conversion for Meshtastic UI Maps, and cache management.

## Features
- Download tiles for custom polygons or the entire world (zoom 0-7).
- Sequential tile download with efficient retry mechanism.
- Convert tiles to 8-bit color depth for Meshtastic UI Maps.
- View and manage cached tiles.
- Configurable map sources via `config/map_sources.json`.

## Prerequisites
- Python 3.8+
- Git

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/map-tile-downloader.git
   cd map-tile-downloader{\rtf1}