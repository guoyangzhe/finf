================================================
PBS for ORCA
================================================
.. code-block:: sh
    :caption: test
    :name: test3
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash

    #PBS -N opt
    #PBS -l nodes=1:ppn=20
    #PBS -l walltime=999:00:00
    #PBS -q n56
    #PBS -r n
    #PBS -e err
    #PBS -o out

    export OMP_NUM_THREADS=1

    JOBNAME=test.inp
    OUTPUTNAME=test.out

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


    source ~/run_software_bashrc/before_run_orca504.sh

    mpirun -np ${NPROCS} orca $JOBNAME > $OUTPUTNAME

    echo "**Finished!"

