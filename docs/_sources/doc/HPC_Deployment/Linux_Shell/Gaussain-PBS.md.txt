# PBS for Gaussian

```bash 
#!/bin/bash
#PBS -l nodes=node1.local:ppn=40
#PBS -l walltime=999:00:00
#PBS -q n56
#PBS -j oe
#PBS -V

unset PATH && \
export PATH=/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/root/bin:$PATH && \
unset LD_LIBRARY_PATH

JOBNAME=td-Ag200-R6G-4.gjf

echo "We work on:"
cat $PBS_NODEFILE
cd $PBS_O_WORKDIR

GAUSS_SCRDIR=/local/scratch/tmp/$PBS_O_LOGNAME/$PBS_JOBID

if [ ! -a $GAUSS_SCRDIR ]; then
   echo "Scratch directory $GAUSS_SCRDIR created."
   mkdir -p $GAUSS_SCRDIR
fi
export GAUSS_SCRDIR
echo "Using $GAUSS_SCRDIR for temporary Gaussian 16 files."
ls -l $GAUSS_SCRDIR

export g16root=/share/apps/gaussian
source $g16root/g16/bsd/g16.profile

cat "$PBS_NODEFILE" |uniq > $GAUSS_SCRDIR/working.nodes
echo "Gaussian16 nodes:"
cat $GAUSS_SCRDIR/working.nodes
export GAUSS_LFLAGS=" -mp 40 -vv -nodefile $GAUSS_SCRDIR/working.nodes"

echo "PBS nodefile:"
echo "++++++++++++++++++++++++++++++++++++"
cat $PBS_NODEFILE
echo "++++++++++++++++++++++++++++++++++++"
#Run a Gaussian command file
echo "Starting Gaussian run at" `date`
time g16 $JOBNAME
echo "Finished Gaussian run at" `date`
echo "Removing GASUU_SCRDIR:"
echo "$GAUSS_SCRDIR"
rm -Rf $GAUSS_SCRDIR
```
