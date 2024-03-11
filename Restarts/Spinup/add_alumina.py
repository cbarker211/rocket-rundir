#!/usr/bin/env python
# Credit Sal Farina

import netCDF4 as nc
import sys
import os

for nam in sys.argv[1:]:
    f = nc.Dataset(nam,mode='a')
    try:
        o = f['SpeciesRst_OCPI']
    except:
        print("SpeciesRst_OCPI not defined")
    f.createVariable("SpeciesRst_AL2O3",o.datatype,dimensions=o.dimensions)
    new = f["SpeciesRst_AL2O3"]
    new[:] = 0.0
    new.long_name= f'Dry mixing ratio of species AL2O3'
    new.units =  o.units
    new.add_offset = 0.0
    new.scale_factor = 1.0
    new.missing_value = 1.0e30
    new.averaging_method = "instantaneous"
    f.close()