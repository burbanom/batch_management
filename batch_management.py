#!/usr/bin/env python

from __future__ import print_function
import os
import re
import sys
import datetime
from subprocess import Popen, PIPE, STDOUT

"""
Below is an example of the job script

    #!/bin/bash

    #
    # Job Submission Script
    #

    #@ class            = queue 
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
    module load mod1 
    module load mod2 
    module load mod3 
    unset LD_PRELOAD

    rm my_env
    env > my_env

    mpirun -np $LOADL_TOTAL_TASKS prog.exe input.inp

"""


class BatchScript:

    def __init__( self, location = './', duration = 3600, ncores = 16, nnodes = 1, executable = 'cp2k.popt', exec_path = None, 
            preamble = None, job_name = 'md', queue = 'clallmds', modules = None,
	exports = None, extras = None, input_file = None, script_type = 'll', mpiexec = 'mpirun -np' ):
        # location refers to the folder where the script will be written
        # duration refers to the time that will be requested in seconds
        # cores refers to the number of cores that will be requested in the script
        # nodes refers to the number of nodes that will be requested in the script
        # executable refers to the executable that will be used
        # job_name is self explanatory
        # queue is the job queue that you want to be assigned (class)
        self.location = str( location )
        self.duration = str( datetime.timedelta( seconds = int(duration)) )
        self.ncores = int( ncores )
        self.nnodes = int( nnodes ) 
        self.executable = str( executable )
        self.job_name = str( job_name )
        self.queue = str( queue )

        if exec_path is None:
            self.exec_path = '' 
        else:
            self.exec_path = str( exec_path )

        if preamble is None:
            self.preamble = [] 
        else:
            self.preamble = preamble 

        if modules is None:
            self.modules = [] 
        else:
            self.modules = modules

        if exports is None:
            self.exports = [] 
        else:
            self.exports = exports 
        if extras is None:
            self.extras = [] 
        else:
            self.extras = extras

        self.script_type = script_type
        self.mpiexec = mpiexec
        self.input_file = input_file


    def create( self ):
        if self.script_type == 'll':
            out_file = open( 'job.sh', 'w' )
            out_file.write( '#!/bin/bash\n' )
            out_file.write( '#@ class            = ' + self.queue + '\n' )
            out_file.write( '#@ job_name         = ' + self.job_name + '\n' )
            out_file.write( '#@ total_tasks      = ' + str( self.ncores ) + '\n' )
            out_file.write( '#@ node             = ' + str( self.nnodes ) + '\n' )
            out_file.write( '#@ wall_clock_limit = ' + self.duration + '\n' )
            out_file.write( '#@ output           = $(job_name).$(jobid).out' + '\n' )
            out_file.write( '#@ error            = $(job_name).$(jobid).err' + '\n' )
            for item in self.preamble:
                out_file.write( '#' + str( item ) + ' \n' )
            out_file.write( '\n' )
            for module in self.modules:
                if module == 'purge':
                    out_file.write( 'module purge\n' )
                else:
                    out_file.write( 'module load ' + str( module ) + '\n' )
            out_file.write( '\n' )
            for extra in self.extras:
                out_file.write( str( extra ) + '\n' )
            out_file.write( '\n' )
            for export in self.exports:
                out_file.write( 'export ' + str( export ) + '\n' )
            out_file.write( '\n' )
            if self.input_file is not None:
                exec_line = str( self.mpiexec ) + ' ' + self.exec_path + self.executable + ' ' + self.input_file + '\n'
            else:
                exec_line = str( self.mpiexec ) + ' ' + self.exec_path + self.executable + '\n' 
            out_file.write(exec_line)
        else:
            print( 'Script type not supported, yet' )

    @classmethod
    def from_dict( cls, options ):

        try:
            options["preamble"] 
        except KeyError:
            preamble = None
        else:
            preamble = filter(len, options["preamble"].split("\n"))

        try:
            options["modules"] 
        except KeyError:
            modules = None
        else:
            modules = filter(len, options["modules"].split("\n"))

        try:
            options["extras"] 
        except KeyError:
            extras = None
        else:
            extras = filter(len, options["extras"].split("\n"))

        try:
            options["exports"] 
        except KeyError:
            exports = None
        else:
            exports = filter(len, options["exports"].split("\n"))

        try:
            options["mpiexec"] 
        except KeyError:
            mpiexec = None
        else:
            mpiexec = filter(len, options["mpiexec"].split("\n"))[0]

        try:
            options["executable"] 
        except KeyError:
            executable = None
        else:
            executable = options["executable"] 

        try:
            options["input_file"] 
        except KeyError:
            input_file = None
        else:
            input_file = options["input_file"]

        return cls( preamble = preamble, modules = modules, exports = exports, extras = extras, mpiexec = mpiexec,
                executable = executable, input_file = input_file ) 

    def check_queue( self ):
        if self.script_type == 'll':
            p = Popen( ['llq'], stdout = PIPE, stderr = PIPE )
            self.q_out, self.q_err = p.communicate()
        else:
            print( 'Script type not supported, yet' )
        return

    def submit_job( self ): 
        if self.script_type == 'll':
            p = Popen( [ 'llsubmit', 'job.sh'], stdout = PIPE, stderr = STDOUT )

            id_holder, self.job_id_err = p.communicate()

            try:
                self.job_id = int( re.findall(r'\b\d+\b', id_holder )[0] )
            except:
                print( 'Unable to retreive job ID' )
        else:
            print( 'Script type not supported, yet' )

        if self.job_id is not None:
            return self.job_id
        else:
            return self.job_id_err
            
    def is_submitted( self ):
        self.job_status()
        if self.status is not None:
             print( re.findall(r'\b\d+\b', self.status ))
        else:
            sys.exit('Unable to establish job status')

    def job_status( self ):
        if self.job_id is not None:
            if self.script_type == 'll':
                self.status = Popen( [ 'llq','-j', str(self.job_id) ] )
            else:
                print( 'Script type not supported, yet' )
        else:
            sys.exit('Unable to establish job status')

