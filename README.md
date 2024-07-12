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
  - Running with SA in stratosphere only (see below#).

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

FH_TOA/no_SA
  - These were additional runs of the main simulation to see how SA affects the results.
  - SA in strat. only is the main run.
  - FDH_TOA run for 2020 Jan-Jul and 2022 Dec.
  - no_SA run for 2020 Jan-May and 2022 Dec.
  - Result is that extending to TOA makes very little difference to our results.

These extra run folders have been moved to the Scratch folder. FDH-stratonly kept in main directory.

So we now have 10-year simulations for the baseline, with smc-only emissions, and with all smc and non-smc emissions.
RRTMG is run for the first three years with SA, and then without RRMTG for 2023-2029. Specific RRTMG runs for Dec 2029 with and without SA.

Now onto sensitivity simulations:
    - Alumina size distribution (YES INCLUDE)
        - Regular simulation is 8% to SMF Al2O3, 8% to DST1 for RTTMG, and 31% to DST2-4.
        - Increase SMF/DST1 to 100% for reentry alumina only, compare effect on RF and O3.
    - Bug fixes (YES INCLUDE)
        - Some minor updates to the emissions have been made since the initial simulations were run.
        - First compare total emissions and calculate % change. 
        - Need to run this with the same re-entry geolocations to be consistent.
        - Compare effect on RF and O3.
    - BC ageing (YES INCLUDE)
        - This is set using an e-folding time to convert BCPO-BCPI. 
        - Switch this off in the stratosphere and mesosphere to see effects.
    - Ozone depletion drivers (YES INCLUDE)
        - Run with only one pollutant at a time, NOx, Cly, Al2O3, CO, H2O, BC
        - Compare effect on O3.
    - Re-entry location (UNSURE)
        - This was tested in Jain's thesis from Seb's group for alumina only, for global vs. south pacific only and for discrete plumes vs. global flux.
        - Found that these had a very small effect on global forcing and lifetime compared to the size distribution.
        - Biggest impact was localised radiative forcing where re-entries were concentrated.
        - We also include NOx, so we would be testing something new. 
        - We do not concentrate re-entries, so RF effects are unlikely.
    - Resolution (YES INCLUDE)
        - 47  vs. 72
        - 4x5 vs. 2x2.5
        - The vertical and horizontal resolutions can be checked first using TransportTracer simulations.
        - Timestep? (UNSURE)
            - We could test whether daily files would be sufficient, but I'm not sure what the benefit would be.
    - Propellant Type (UNSURE)
        - This would be similar to the O3 sensitivity simulations, and would provide an interesting result on the individual RF/O3 impacts of each propellant. 
        - My approach would be to only include emissions from specific launches, but you could also do this by switching all launches to have a single propellant.
        - Would require 4 simulations (methane not really worth it as its only one launch).


  
