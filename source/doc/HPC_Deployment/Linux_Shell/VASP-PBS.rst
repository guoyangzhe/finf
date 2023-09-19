=====================================
PBS for VASP
=====================================

.. code-block:: sh
    :caption: vasp-pbs
    :name: test7
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

    # export OMP_NUM_THREADS=2

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

    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/bin/mklvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/ifortvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/iccvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mpi/intel64/bin/mpivars.sh intel64

    export GNU_HOME=/opt/ohpc/pub/compiler/gcc/8.3.0 && \
    export PATH=$GNU_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$GNU_HOME/lib:$GNU_HOME/lib64:$LD_LIBRARY_PATH && \
    export INCLUDE=$GNU_HOME/include:$INCLUDE

    export CUDA_HOME=/share/apps/nvidia/cuda/cuda-11.1 && \
    export PATH=$CUDA_HOME/bin:$PATH && \
    export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH && \
    export INCLUDE=$CUDA_HOME/include:$INCLUDE

    mpirun -n $NPROCS /share/apps/vasp/intel-vasp/5.4.4.pl2/bin/vasp_std >& screen.log
    #mpirun -n $NPROCS /share/apps/vasp/intel-vasp/6.1.0/bin/vasp_std >& screen.log

    echo "**Finished!"
