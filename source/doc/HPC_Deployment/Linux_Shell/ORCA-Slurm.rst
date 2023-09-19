================================================
Slurm for ORCA
================================================
.. code-block:: sh
    :caption: test
    :name: test5
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash
    #SBATCH -J orca-opt
    #SBATCH -o %J.out
    #SBATCH -e %J.err
    #SBATCH -N 1
    #SBATCH -w node01
    #SBATCH -n 36
    #SBATCH -t 999:0:0
    #SBATCH -p hpc

    export OMP_NUM_THREADS=1

    JOBNAME=test.inp
    OUTPUTNAME=test.out

    echo Time is `date`
    echo Working dir is $SLURM_SUBMIT_DIR  #$SLURM_SUBMIT_DIR：作业提交目录
    cd $SLURM_SUBMIT_DIR

    NPROCS=$((SLURM_NTASKS))  #$SLURM_NTASKS：总任务数
    N_NODE=$((SLURM_JOB_NUM_NODES))  #$SLURM_JOB_NUM_NODES：节点数

    echo This job has allocated ${N_NODE} nodes with ${NPROCS} processors
    echo Running on host `hostname`
    echo This jobs runs on the following processors:
    echo "**Start"

    echo $SLURM_SUBMIT_DIR > work.txt
    echo $SLURM_NODELIST > nodefile.txt   #$SLURM_NODELIST：节点列表
    echo $NPROCS > cpucore.txt
    echo $N_NODE > node.txt

    source ~/run_software_bashrc/before_run_orca504.sh

    mpirun -np ${NPROCS} orca $JOBNAME > $OUTPUTNAME

    echo "**Finished!"

