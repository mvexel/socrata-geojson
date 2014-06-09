socrata-geojson
===============

Convert the data from a Socrata SODA 'geo' json endpoint to actual geoJSON

## Installation

    pip install -r requirements.txt

## Usage

    python parse-socrata-json.py URL OUTFILE

You will end up with a valid GeoJSON file that contains all the objects from the Socrata response that have a location.

Try it with

    python parse-socrata-json.py\
    https://data.cityofchicago.org/resource/alternative-fuel-locations.json?fuel_type_code=CNG\
    ~/tmp/demo.geojson

![example](https://www.dropbox.com/s/k1qmtcy1z7s5sb1/Screenshot%202014-06-09%2011.25.20.png)