# ecmwf-hacking
Scripts to download and parse GRIB files and turn them into CSV

## Installation

conda env create -f environment.yml
source activate grib

1. Run/edit get_tigge_forecasts.py and get_landsea_mask.py.
2. Run convert.sh. This should create a folder data.
3. Use concat.py to concatenate the files.
