#!/bin/bash
#SBATCH --job-name=torch_check_installed_and_available_ram
#SBATCH --output=torch_check_output_%j.txt
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:15:00
#SBATCH --partition=gpu06

module purge
module load python/miniforge-24.3.0
conda activate pytorch-el7-24.3.0
python torch_check/if_torch_installed_and_available_ram.py
