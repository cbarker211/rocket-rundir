# This run directory is for GEOS-Chem Classic.

## For instructions on setting up, compiling, and running GEOS-Chem Classic, see:

  - https://geos-chem.readthedocs.org

## For additional information about GEOS-Chem, see:

  - http://wiki.geos-chem.org

  - http://geos-chem.org

## For help with GEOS-Chem Classic, see:

  - https://geos-chem.readthedocs.io/en/latest/reference/SUPPORT.html

  - https://geos-chem.readthedocs.io/en/latest/reference/CONTRIBUTING.html

Main rundir for rocket simulations.
Initial 5 month spinup with v14.3.0 chemistry (no alumina additions) and v14.1.1 restart files to spinup the new species.
  - geoschem_config_spinup.yml
    - updated start/end time
    - updated cloudj source location
  - HEMCO_Config_spinup.rc
    - added rockets but disabled
    - GEOS-Chem restart flag set as EFYO.
    - Updated restart locations to the spinup folder.
    - Changed GFED locaiton to the 2020-02 folder and time range end to 2019. Will update when we get to 2020.
  - HISTORY.rc
    - Updated restart and output locations to the spinup folders. Aerosol and ConcAfterChem collections turned on.
  - Restart files
    - Copied from the the spinup rundir for 20190801. Made copies so I can manually add new species.
