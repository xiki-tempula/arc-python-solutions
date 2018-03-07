#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:05:00
#SBATCH --job-name=integral

module purge
module load python/anaconda2/5.0.1
module load gcc/5.3.0

mpiexec -n 4 python integral_mpi.py
