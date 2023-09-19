Slurm for GPAW
=================================

script1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh
    :caption: gpaw_slurm.sh
    :name: test1
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash
    #SBATCH -J al201-gs
    #SBATCH -o %J.out
    #SBATCH -e %J.err
    #SBATCH -N 1
    #SBATCH -w node01
    #SBATCH -n 16
    #SBATCH -t 999:0:0
    #SBATCH -p debug01

    export OMP_NUM_THREADS=1

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

    export STARTTIME=`date +%s.%3N`
    export WALLTIME=`squeue -h -o %l -j $SLURM_JOB_ID`

    source ~/.bashrc
    source ~/run_software_bashrc/before_run_gpaw22.8.0.sh

    #srun gpaw -P python gs.py
    mpiexec -np ${NPROCS} gpaw python gs.py

    echo "**Finished!"


script2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh
    :caption: gpaw_slurm.sh
    :name: test2
    :emphasize-lines: 2
    :linenos:

    #!/bin/bash
    #SBATCH -J al201-gs
    #SBATCH -o %J.out
    #SBATCH -e %J.err
    #SBATCH -N 1
    #SBATCH -w node01
    #SBATCH -n 16
    #SBATCH -t 999:0:0
    #SBATCH -p debug01

    export OMP_NUM_THREADS=1

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

    export STARTTIME=`date +%s.%3N`
    export WALLTIME=`squeue -h -o %l -j $SLURM_JOB_ID`

    source ~/.bashrc
    source ~/run_software_bashrc/before_run_gpaw22.8.0.sh

    start_time=$(date +%s)

    # 开始第一个计算任务
    task_start_time=$(date +%s)
    # 执行第一个计算任务的命令
    mpiexec -np ${NPROCS} gpaw python timepropagation_calculate.py
    # 计算第一个计算任务的耗时
    task_duration=$(( $(date +%s) - $task_start_time ))
    echo "Task 1 duration: $task_duration seconds" > total_time.txt

    # 开始第二个计算任务
    task_start_time=$(date +%s)
    # 执行第二个计算任务的命令
    mpiexec -np ${NPROCS} gpaw python timepropagation_continue.py
    # 计算第二个计算任务的耗时
    task_duration=$(( $(date +%s) - $task_start_time ))
    echo "Task 2 duration: $task_duration seconds" > total_time.txt

    # 开始第二个计算任务
    task_start_time=$(date +%s)
    # 执行第二个计算任务的命令
    mpiexec -np ${NPROCS} gpaw python timepropagation_postprocess.py
    # 计算第二个计算任务的耗时
    task_duration=$(( $(date +%s) - $task_start_time ))
    echo "Task 3 duration: $task_duration seconds" > total_time.txt

    # 开始第二个计算任务
    task_start_time=$(date +%s)
    # 执行第二个计算任务的命令
    python timepropagation_plot.py
    # 计算第二个计算任务的耗时
    task_duration=$(( $(date +%s) - $task_start_time ))
    echo "Task 4 duration: $task_duration seconds" > total_time.txt

    end_time=$(date +%s)
    duration=$(( $end_time - $start_time ))
    echo "Total duration: $duration seconds" > total_time.txt
    echo "**Finished!"

script3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh
    :caption: gpaw_slurm.sh
    :name: test20
    :emphasize-lines: 20
    :linenos:

    #!/bin/bash
    #SBATCH -J gs-fd-Mg8
    #SBATCH -o %J.out
    #SBATCH -e %J.err
    #SBATCH -N 1
    #SBATCH -w node01
    #SBATCH -n 56
    #SBATCH -t 30-12:00:00
    #SBATCH -p hpc
    #=======================
    export OMP_NUM_THREADS=1
    #=======================
    echo =======================
    echo Submit Time is [`date`].
    echo Working dir is [$SLURM_SUBMIT_DIR].
    cd $SLURM_SUBMIT_DIR
    NPROCS=$((SLURM_NTASKS))
    N_NODE=$((SLURM_JOB_NUM_NODES))
    echo This job has allocated [${N_NODE}] nodes with [${NPROCS}] processors.
    echo Running on host [`hostname`].
    echo This jobs runs on the following processors:
    echo =======================
    echo "**Start!!!"
    echo Job start Time is [`date`].
    # echo "Submit Direction is "$SLURM_SUBMIT_DIR >> $SLURM_JOB_ID.out
    # echo "Submit NodeList is "$SLURM_NODELIST >> $SLURM_JOB_ID.out
    # echo "Submit CPU_Cores is "$NPROCS >> $SLURM_JOB_ID.out
    # echo "Submit N_Node is "$N_NODE >> $SLURM_JOB_ID.out
    echo This job name is [$SLURM_JOB_NAME] and job id is [$SLURM_JOB_ID]. >> $SLURM_JOB_ID.out
    #=======================
    # export STARTTIME=`date +%s.%3N` # start time
    # export WALLTIME=12:00:00  # wall time
    export STARTTIME=`date +%s.%3N`
    export WALLTIME=`squeue -h -o %l -j $SLURM_JOB_ID`
    source ~/.bashrc
    source /data1/soft_bashrc/before_run_gpaw22.8.0.sh

    start_time=$(date +%s)
    #1
    task_start_time=$(date +%s)
    mpiexec -np ${NPROCS} gpaw python gs.py 
    # mpiexec -np ${NPROCS} gpaw python gsc.py
    task_duration=$(( $(date +%s) - $task_start_time ))
    echo "Task 1 duration: $task_duration seconds." >> $SLURM_JOB_ID.out
    end_time=$(date +%s)
    duration=$(( $end_time - $start_time ))
    echo "Total duration: $duration seconds." >> $SLURM_JOB_ID.out

    echo Job finish Time is [`date`].
    echo "**Finished!!!"
    echo =======================
    echo "                       "
