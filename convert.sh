grib_get_data -F %.4f -p date,step,stepRange,shortName landseamask | python grib2csv.py lsm

grib_get_data -F %.4f -p date,step,stepRange,shortName 2012cf | python grib2csv.py 2012cf

grib_get_data -F %.4f -p date,step,stepRange,shortName 2013cf | python grib2csv.py 2013cf

grib_get_data -F %.4f -p date,step,stepRange,shortName 2012fc | python grib2csv.py 2012fc

grib_get_data -F %.4f -p date,step,stepRange,shortName 2013fc | python grib2csv.py 2013fc