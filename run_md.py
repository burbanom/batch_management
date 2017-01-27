#! /usr/bin/env python

# Contributors:
# Mario Burbano (burbano.carmona@gmail.com)

from __future__ import print_function, division
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
from os.path import isfile
import sys
from subprocess import call, check_output, CalledProcessError
from datetime import datetime, timedelta
import time

"""
Program for performing MD simulations
"""
__author__ = "Mario Burbano"
__credits__ = ["Mario Burbano"]
__maintainer__ = "Mario Burbano"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "burbano.carmona@gmail.com"
__date__ = "27 Jan., 2017"
__status__ = "Production"


def parse_commandline_arguments():
    parser = argparse.ArgumentParser( description = 'Program for continously running MD simulations' )
    parser.add_argument( '--job', '-j', metavar = 'S', type=str, required = True, help='Sample job script' )
    parser.add_argument( '--hours', '-ho', metavar = 'N', type=int, required = True, help='Number of hours between after which command will be executed' )
    parser.add_argument( '--seconds', '-s', metavar = 'N', type=int, required = True, help='Number of seconds between after which command will be executed' )
    parser.add_argument( '--wait', '-w', metavar = 'N', type=int, required = True, help='Number of seconds that program will wait' )
    #parser.add_argument( '--msdlen', '-ml', metavar = 'N', type=int, required = True, help='Length of msd' )
    #parser.add_argument( '--prntfrq', '-p', metavar = 'N', type=int, required = False, default = 1000, help='Print frequency of displacements' )
    #parser.add_argument( '--timestep', '-t', metavar = 'F', type=float, required = False, default = 41.3414, help='Simulation timestep in a.u.' )
    #parser.add_argument( '--displacement-file', '-d', help='complete displacement file filename', default='displong.out.gz' )
    #parser.add_argument( '--msd-files', '-m', nargs='+', help='list of msd output files to analyse', required = True )
    #parser.add_argument( '--convcalc', '-cc', action='store_true', help='Perform a slope convergence calculation rather than the slope statistics calculation.' )
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    my_cmd = args.job
    interval_hours = args.hours
    interval_seconds = args.seconds
    max_loops = 1000
    sleep_time = args.wait

    for loop in range(max_loops):
	
	start_time = datetime.now()
	dt = start_time + timedelta(hours=interval_hours, seconds=interval_seconds)

	while (datetime.now() < dt):
            print( str( loop ) + ' sleep' )
	    time.sleep(sleep_time)

	else:
	    if ( datetime.now().hour <= 17 ) and ( datetime.now().minute < 10 ):
                cmd_output = check_output( my_cmd, shell = True ) 
                print('else' )
                print( cmd_output )
