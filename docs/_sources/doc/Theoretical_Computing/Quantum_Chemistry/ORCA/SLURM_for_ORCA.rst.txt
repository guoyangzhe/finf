SLURM script file for ORCA
================================================
.. code-block:: sh
    :caption: test
    :name: test9
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash -l
    # Section for defining queue-system variables:
    # SLURM-section
    #SBATCH --job-name=thi_05
    #SBATCH --output=thi_05.slurmout
    #SBATCH --partition=debug_1,cluster8
    #SBATCH --nodes=1
    #SBATCH --ntasks=8
    #SBATCH --ntasks-per-socket=4
    #SBATCH --cpus-per-task=1
    #SBATCH --threads-per-core=1
    #SBATCH --mem-per-cpu=2000
    ######################################
    # Section for defining job variables and settings:
    LD_LIBRARY_PATH="/usr/local/openmpi-2.1.1/build/lib64"
    PATH="/bin:/usr/bin:/usr/local/openmpi-2.1.1/build/bin"
    export ORCA_DIR=/scr1/orca_4_0_0_2_linux_x86-64/
    export PATH=$PATH:$ORCA_DIR
    LaunchDir=$PWD;

    #create a local working directory for the ORCA calculation
    ORCA_SCRDIR="/scr1/"$USER"/"$SLURM_JOB_ID""
    mkdir -p $ORCA_SCRDIR

    #Copy the input file to the local working directory
    cp $LaunchDir/$SLURM_JOB_NAME.inp  $ORCA_SCRDIR/$SLURM_JOB_NAME.inp

    #Start ORCA
    /scr1/orca_4_0_0_2_linux_x86-64/orca  $ORCA_SCRDIR/$SLURM_JOB_NAME.inp > $LaunchDir/$SLURM_JOB_NAME.out

    # after ORCA is finished move the gbw file back to the home directory and generate molden input
    mv $ORCA_SCRDIR/$SLURM_JOB_NAME.gbw $LaunchDir/$SLURM_JOB_NAME.gbw
    /scr1/orca_4_0_0_2_linux_x86-64/orca_2mkl $LaunchDir/$SLURM_JOB_NAME  -molden

    # After finishing successfully clean up the local working directory
    rm -rf $ORCA_SCRDIR

    exit 0

