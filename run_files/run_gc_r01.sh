#!/bin/bash -l

# Short script to compile GEOS-Chem v12.9.3 using CMake.

# Settings for batch job on UCL Legion:
#$ -S /bin/bash
#$ -l h_rt=72:00:00
#$ -l mem=1G
#$ -N r01
#$ -j y  
#$ -pe smp 12
#$ -V -cwd
#$ -P hpc.10
#$ -l paid=1
#$ -M connor.barker@ucl.ac.uk
#$ -m bea

# Get relevant environmental variables defined in .bashrc file:
source ~/.bashrc_gc

# Set path to spack modules:
#source /etc/profile.d/modules.sh

# Clear module list to avoid conflicts:
#module purge
# Load relevant libraries:
#module load /lustre/projects/uptrop/spack/share/spack/modules/linux-rhel7-broadwell/gcc-9.2.0-gcc-4.9.2-ypebi5t
#module load /lustre/projects/uptrop/spack/share/spack/modules/linux-rhel7-skylake_avx512/netcdf-fortran-4.5.3-gcc-9.2.0-lqhzcio
#module load /lustre/projects/uptrop/spack/share/spack/modules/linux-rhel7-skylake_avx512/openmpi-3.1.6-gcc-9.2.0-vdsobny
#module list

#spack load gcc
#spack load netcdf-fortran
#spack load openmpi
#spack find --loaded

# Limits and stacksizes required:
ulimit -s unlimited
export OMP_STACKSIZE=512M

# Set up dependencies:
ln -sf ./HEMCO_Config.rc.gmao_metfields_r01 HEMCO_Config.rc.gmao_metfields
ln -sf ./species_database_alumina.yml species_database.yml
ln -sf ./geoschem_config_r01.yml geoschem_config.yml
ln -sf ./HEMCO_Config_r01.rc HEMCO_Config.rc
ln -sf ./HISTORY_r01.rc HISTORY.rc


# Pipe output to log file only:
./gcclassic > ./logs/Rockets/log_gc_r01
#./gcclassic --dryrun > ./logs/Rockets/log_gc_r01_dryrun
# Clean up:
unset id
unset nodename

# Exit normally:
exit 0
