=====================================
PBS for CP2K
=====================================

.. code-block:: sh
    :caption: cp2k-pbs
    :name: tests
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash
    #PBS -N cp2k-test
    #PBS -l nodes=1:ppn=36
    #PBS -l walltime=999:00:00
    #PBS -q n56
    #PBS -j oe
    #PBS -V
    JOBNAME=test.inp

    cd $PBS_O_WORKDIR

    #source ~/.bashrc
    source /share/apps/intel/intel-2018up4/parallel_studio_xe_2018/bin/psxevars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mkl/bin/mklvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/ifortvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/bin/iccvars.sh intel64 && \
    source /share/apps/intel/intel-2018up4/compilers_and_libraries_2018.5.274/linux/mpi/intel64/bin/mpivars.sh intel64

    source /share/apps/cp2k/gnu/install/setup
    export PATH=/share/apps/cp2k/gnu/exe/local:${PATH}



    #source /opt/env-intel.sh
    #ulimit -s unlimited
    export LD_LIBRARY_PATH=/share/apps/cp2k/gnu/install/elpa-2020.11.001/cpu/lib:$LD_LIBRARY_PATH
    mpirun -np 36 /share/apps/cp2k/gnu/exe/local/cp2k.popt $JOBNAME > test_pbs.out




