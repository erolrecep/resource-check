#!/bin/bash
#SBATCH --job-name=tf_check_installed_and_available_ram
#SBATCH --output=tf_check_output_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00

module purge
module load python/
python tf_check/if_tf_installed_and_available_ram.py
