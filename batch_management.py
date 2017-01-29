#!/usr/bin/env python

import os
from subprocess import check_output, STDOUT
from ase.io.vasp import read_vasp,read_vasp_out

"""
Below is an example of the job script

    #!/bin/bash

    #
    # Job Submission Script for Poincare
    #

    #@ class            = clallmds
    #@ job_name         = md 
    #@ total_tasks      = 1
    #@ node             = 1
    #@ wall_clock_limit = 04:00:00
    #@ output           = $(job_name).$(jobid).log
    #@ error            = $(job_name).$(jobid).err
    #@ job_type         = mpich
    #@ environment      = COPY_ALL
    #@ queue

    module purge
    module load intel-env/15.0.0 intelmpi/5.0.1 lapack/3.5_intel15 mkl/11.2
    module load autotools/Feb2014
    module load python/anaconda-2.3.0
    unset LD_PRELOAD

    rm my_env
    env > my_env

    export PYTHONPATH=/gpfshome/mds/staff/mburbano/Source/ase:$PYTHONPATH
    export PYTHONPATH=/gpfshome/mds/staff/mburbano/Source/pycp2k:$PYTHONPATH

    mpirun -np $LOADL_TOTAL_TASKS /gpfs1l/gpfshome/mds/staff/mburbano/Source/cp2k-3.0_modif/exe/Linux-x86-64-intel/cp2k.popt input-restart.inpt  >> md.out 

"""


class batch_script:

    def __init__( self, location = './', duration = 3600, ncores = 16, nnodes = 1, executable = 'cp2k.popt', exec_path = './', job_name = 'md', queue = 'clallmds', modules = [] ):
        # location refers to the folder where the script will be written
        # duration refers to the time that will be requested in seconds
        # cores refers to the number of cores that will be requested in the script
        # nodes refers to the number of nodes that will be requested in the script
        # executable refers to the executable that will be used
        # job_name is self explanatory
        # queue is the job queue that you want to be assigned (class)
        self.location = str( location )
        self.duration = int( duration )
        self.ncores = int( ncores )
        self.nnodes = int( nnodes ) 
        self.executable = str( executable )
        self.exec_path = str( exec_path )
        self.job_name = str( job_name )
        self.queue = str( queue )
        self.modules = modules

    def create_ll( self ):
        out_file = open( 'job.sh', 'w' )
        out_file.write( '#!/bin/bash\n' )
        out_file.write( '#@ class            = ' + self.queue + '\n' )
        out_file.write( '#@ job_name         = ' + self.job_name + '\n' )
        out_file.write( '#@ total_tasks      = ' + str( self.ncores ) + '\n' )
        out_file.write( '#@ node             = ' + str( self.nnodes ) + '\n' )
        out_file.write( '#@ wall_clock_limit = ' + '0:00:' + str( self.duration ) + '\n' )
        out_file.write( '#@ output           = $(job_name).$(jobid).log' + '\n' )
        out_file.write( '#@ error            = $(job_name).$(jobid).err' + '\n' )
        out_file.write( '#@ job_type         = mpich' + '\n' )
        out_file.write( '#@ environment      = COPY_ALL' + '\n' )
        out_file.write( '#@ queue' + '\n' )
        out_file.write( 'module purge\n' )
        out_file.write( 'module load intel-env/15.0.0 intelmpi/5.0.1 lapack/3.5_intel15 mkl/11.2\n' )
        out_file.write( 'module load autotools/Feb2014\n' )
        out_file.write( 'module load python/anaconda-2.3.0\n' )
        out_file.write( 'unset LD_PRELOAD\n' )
        out_file.write( '\n' )
        out_file.write( 'export PYTHONPATH=/gpfshome/mds/staff/mburbano/Source/ase:$PYTHONPATH\n' )
        out_file.write( 'export PYTHONPATH=/gpfshome/mds/staff/mburbano/Source/pycp2k:$PYTHONPATH\n' )
        out_file.write( 'mpirun -np $LOADL_TOTAL_TASKS ' + self.exec_path +
                self.executable + ' ' + self.job_name +'.inp\n' )

    def check_queue( self , command = 'llq' ):
        self.theq = check_output( [ command ], stderr = STDOUT )
        return

    def submit_job( self , sub_command = 'llsubmit' ): 
        self.submit = check_output( [ sub_command , 'job.sh'] )

    def job_status( self, status_command = 'llq -j' ):
        self.status = check_output( [ status_command, self.job_id ] )

