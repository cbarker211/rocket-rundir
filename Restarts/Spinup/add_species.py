#!/usr/bin/env python
# Credit Sal Farina

import netCDF4 as nc
import sys
import os

new_species = ['SpeciesRst_PSO4AQ', 'SpeciesRst_PH2SO4', 'SpeciesRst_TSOG3', 'SpeciesRst_TSOG2',
               'SpeciesRst_TSOG1', 'SpeciesRst_TSOG0', 'SpeciesRst_TSOA3', 'SpeciesRst_TSOA2',
               'SpeciesRst_TSOA1', 'SpeciesRst_TSOA0', 'SpeciesRst_FURA', 'SpeciesRst_BUTDI',
               'SpeciesRst_ASOG3', 'SpeciesRst_ASOG2', 'SpeciesRst_ASOG1', 'SpeciesRst_ASOAN',
               'SpeciesRst_ASOA3', 'SpeciesRst_ASOA2', 'SpeciesRst_ASOA1']

for nam in sys.argv[1:]:
    f = nc.Dataset(nam,mode='a')
    try:
        o = f['SpeciesRst_OCPI']
    except:
        print("SpeciesRst_OCPI not defined")
    for species in new_species:
        species_name = species.replace("SpeciesRst_","")
        f.createVariable(species,o.datatype,dimensions=o.dimensions)
        new = f[species]
        new[:] = 0.0
        new.long_name= f'Dry mixing ratio of species {species.replace("SpeciesRst_","")}'
        new.units =  o.units
        new.add_offset = 0.0
        new.scale_factor = 1.0
        new.missing_value = 1.0e30
        new.averaging_method = "instantaneous"
    f.close()