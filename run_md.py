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
import subprocess
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
    parser.add_argument( '--job', '-j', metavar = 'S', type=str, required = False, help='Sample job script' )
    #parser.add_argument( '--offset', '-so', metavar = 'N', type=int, required = True, help='Offset (in number of frames) between the slices or increment in conv. calc.' )
    #############################################################################################################################################
    #parser.add_argument( '--msdlen', '-ml', metavar = 'N', type=int, required = True, help='Length of msd' )
    #parser.add_argument( '--prntfrq', '-p', metavar = 'N', type=int, required = False, default = 1000, help='Print frequency of displacements' )
    #parser.add_argument( '--timestep', '-t', metavar = 'F', type=float, required = False, default = 41.3414, help='Simulation timestep in a.u.' )
    #parser.add_argument( '--displacement-file', '-d', help='complete displacement file filename', default='displong.out.gz' )
    #parser.add_argument( '--msd-files', '-m', nargs='+', help='list of msd output files to analyse', required = True )
    #parser.add_argument( '--convcalc', '-cc', action='store_true', help='Perform a slope convergence calculation rather than the slope statistics calculation.' )
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    interval_hours = 0
    interval_seconds = 10
    max_loops = 1000
    sleep_time = 2

    for loop in range(max_loops):
	
	start_time = datetime.now()
	dt = start_time + timedelta(hours=interval_hours, seconds=interval_seconds)

	while (datetime.now() < dt):
	    print( str( loop ) + ' sleep' )
	    time.sleep(sleep_time)

	else:
	    if ( datetime.now().hour <= 17 ) and ( datetime.now().minute < 10 ):
		print( 'else clause' )
		print( datetime.now() )
