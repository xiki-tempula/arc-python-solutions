#!/bin/bash

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:10:00
#SBATCH --job-name=pyTest
#SBATCH --partition=devel

module purge
module load python/anaconda2/5.0.1
module load gcc/5.3.0

mpiexec -np 32  python darts_mpi.py
