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

Three simulations running together - Baseline (b), Rockets (r), and SMC (s).
  - Baseline outputs the DynHeating collection, which the rocket simulations require for RRTMG stratospheric adjustment.
  - Symbolic link in main folder points here (see https://github.com/geoschem/geos-chem/pull/2010)
  - Rockets/SMC input the DynHeating files, added to HEMCO_Config.rc.gmao_metfields

b01/r01/s01
  - January 2020

b02/r02
  - February 2020 - May 2020.
  - Changed HEMCO log file and geoschem date range.

b03/r03
  - Up to Dec 2020 (want to make sure if there are any issues heading into 2021 that we don't have to rerun the whole thing.)
  - Changed HEMCO log file and geoschem date range.
  - Updated GMD_SFC_CH4 with new files up to end of 2022.

b04/r04
  - Dec 2020 - Jun 2021
  - Changed HEMCO log file and geoschem date range.
  - Added RRTMG output for O3T and H2O to HISTORY.rc

b05/r05
  - Jul 2021 - Dec 2021
  - Changed HEMCO log file and geoschem date range.

b06/r06
  - Jan 2022 - Jun 2022
  - Changed HEMCO log file and geoschem date range.

b07/r07
  - Jul 2022 - Nov 2022
  - Changed HEMCO log file and geoschem date range.

b08/r08
  - Dec 2022
  - Changed HEMCO log file and geoschem date range.
  - Updated LightNox code from RFY3 to CY in HEMCO_Config.rc.gmao_metfields.
  - Offline Dust code changed from EFY to CY in HEMCO_Config.rc.
  - Rockets code changed from EFY to C in HEMCO_Config.rc.

Realised after running for the full three years that there was a bug in the emission inventories,
where some stage mass for Atlas had been massively inflated. So had to re-run from r03 onwards. 

co2check
  - This was to make sure the stratospheric adjustment was working correctly.
  - Perturbation of +100 ppmv CO2, without SA, with SA and with SA up to TOA.