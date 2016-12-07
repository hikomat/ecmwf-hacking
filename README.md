# ecmwf-hacking
Scripts to download and parse GRIB files and turn them into CSV

1. Use ecmwf conda environment to download GRIB files. Simply run get_tigge_forecasts.py and get_landsea_mask.py.
2. Use grib conda environment to convert GRIB into CSV. Run convert.sh. This should create a folder data.
3. Use concat.py to concatenate the files. pandas is a prerequisit, so use the conda environment where it is installed.
