#!/bin/bash
#SBATCH --job-name=torch_check_installed_and_available_ram
#SBATCH --output=torch_check_output_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00

module purge
module load python/
python torch_check/if_torch_installed_and_available_ram.py
