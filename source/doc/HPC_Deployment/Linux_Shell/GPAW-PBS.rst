=====================================
PBS for GPAW
=====================================

.. code-block:: sh
    :caption: test
    :name: test10
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash

    #PBS -N Al201
    #PBS -l nodes=1:ppn=56
    #PBS -l walltime=12:00:00
    #PBS -q n56
    #PBS -r n
    #PBS -e err
    #PBS -o out

    export OMP_NUM_THREADS=1

    echo Time is `date`
    echo Working dir is $PBS_O_WORKDIR
    cd $PBS_O_WORKDIR

    NPROCS=`wc -l < ${PBS_NODEFILE}`
    N_NODE=`uniq ${PBS_NODEFILE}|wc -l`

    echo This job has allocated ${N_NODE} nodes with ${NPROCS} processors
    echo Running on host `hostname`
    echo This jobs runs on the following processors:
    echo "**Start"

    echo $PBS_O_WORKDIR > work.txt
    echo ${PBS_NODEFILE} > nodefile.txt
    echo $NPROCS > cpucore.txt
    echo $N_NODE > node.txt

    source ~/.bashrc  #加载.bashrc文件  加载GPAW环境变量

    export STARTTIME=`date +%s.%3N` # start time
    export WALLTIME=12:00:00  # wall time

    mpiexec -np ${NPROCS} gpaw python gs.py 
    #mpiexec -np ${NPROCS} gpaw python gsc.py

    echo "**Finished!"

