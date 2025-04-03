from setuptools import setup, find_packages

setup(
    name="map-tile-downloader",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask",
        "flask-socketio",
        "requests",
        "mercantile",
        "shapely",
        "pillow"
    ],
    entry_points={
        "console_scripts": [
            "map-tile-downloader = tileDL:main"
        ]
    }
)