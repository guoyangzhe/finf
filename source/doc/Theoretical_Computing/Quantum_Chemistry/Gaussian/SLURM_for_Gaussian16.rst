=====================================================
SLURM script file for Gaussian 16
=====================================================

.. code-block:: sh
    :caption: test
    :name: test333
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash -l
    # Section for defining queueing system variables:
    # SLURM-section
    #SBATCH --job-name=watdim01    
    #SBATCH --output=watdim01.slurmout
    #SBATCH --partition=cluster8                
    #SBATCH --nodes=1
    #SBATCH --cpus-per-task=8
    #SBATCH --threads-per-core=1
    #SBATCH --mem-per-cpu=2000
    ######################################
    # Section for defining job variables and settings:
    g16root="/scr1/g16_a.03_sse4"
    g16dir="/scr1/g16_a.03_sse4/g16"
    LaunchDir=$PWD;
    LocalRunDir=/scr1/$USER/$SLURM_JOB_ID
    export GAUSS_SCRDIR=$LocalRunDir;
    mkdir -p $GAUSS_SCRDIR
    export GAUSS_EXEDIR=$g16dir
    export GAUSS_ARCHDIR=$g16dir
    cat >/$LocalRunDir/$SLURM_JOB_NAME.gjf <<EOF
    %chk=$GAUSS_SCRDIR/$SLURM_JOB_NAME.chk
    %CPU=0-7       
    %mem=16000MB
    #p b3lyp/6-31+G(d,p) opt=(Z-Matrix) iop(1/7=30) int=ultrafine  EmpiricalDispersion=GD3 

    watdim01 water dimer b3lyp-D3/6-31+G(d,p) opt tight Cs, int=ultrafine    

    0 1
    O1
    H2  1  r2
    H3  1  r3  2  a3
    X4  2  1.0  1  90.0  3  180.0
    O5  2  r5  4  a5  1  180.0
    H6  5  r6  2  a6  4  d6
    H7  5  r6  2  a6  4  -d6

    r2=0.9732       
    r3=0.9641      
    r5=1.9128    
    r6=0.9659   
    a3=105.9    
    a5=83.1         
    a6=112.1       
    d6=59.6         


    EOF
    $g16dir/g16 < $GAUSS_SCRDIR/$SLURM_JOB_NAME.gjf > $LaunchDir/$SLURM_JOB_NAME.log
    cp $GAUSS_SCRDIR/$SLURM_JOB_NAME.chk $LaunchDir/
    # The following line will clean up /scr1 after finishing the job
    rm -rf $LocalRunDir
    # If your job finishes normally, delete the empty .slurmout file
    slurmout_check=`cat $SLURM_JOB_NAME.slurmout`
    if [$slurmout_check = ""]; then
    rm -f $SLURM_JOB_NAME.slurmout
    fi

    exit 0