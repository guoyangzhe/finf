# Slurm for Gaussian

```bash 
#!/bin/bash
#SBATCH -J g16-opt
#SBATCH -o %J.out
#SBATCH -e %J.err
#SBATCH -N 1
#SBATCH -w node01
#SBATCH -n 36
#SBATCH -t 999:0:0
#SBATCH -p hpc

source /home/gn/run_software_bashrc/before_run_gaussian_gn.sh

JOB_NAME=N

g16 ${JOB_NAME}.gjf > ${JOB_NAME}.out

formchk ${JOB_NAME}.chk
```
