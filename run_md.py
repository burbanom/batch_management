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
__status__ = "Experimental"


def parse_commandline_arguments():
    parser = argparse.ArgumentParser( description = 'Program for continously running MD simulations' )
    parser.add_argument( '--job', '-j', metavar = 'S', type=str, required = True, help='Sample job script' )
    parser.add_argument( '--maxloops', '-ml', metavar = 'N', type=int, required = False, default = 1000, help='maximum number of loops for the script to run' )
    parser.add_argument( '--seconds', '-s', metavar = 'N', type=int, required = True, help='Number of seconds between after which command will be executed' )
    parser.add_argument( '--wait', '-w', metavar = 'N', type=int, required = False, help='Number of seconds that program will wait' )
    parser.add_argument( '--starttime', '-st', metavar = 'N', type=int, required = False, default = 17, help='Hour from which jobs can be submitted' )
    parser.add_argument( '--endtime', '-et', metavar = 'N', type=int, required = False, default = 8, help='Hour up to which jobs can be submitted' )
    parser.add_argument( '--debug', '-d', metavar = 'B', type=bool, required = False, default=False, help='Print debug messages?' )
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    my_cmd = args.job
    interval_seconds = args.seconds
    max_loops = args.maxloops
    if args.wait is not None:
        sleep_time = args.wait
    else:
        sleep_time = int( interval_seconds / 2 )
        if sleep_time <= 0:
            sleep_time = 1
    debug = args.debug
    start_time = args.starttime
    end_time = args.endtime

    for loop in range(max_loops):
	
	initial_time = datetime.now()
	dt = initial_time + timedelta(seconds=interval_seconds)

	while (datetime.now() < dt):
            if debug:
                print( str( loop ) + ' sleep' )
	    time.sleep(sleep_time)

	else:
            if ( datetime.now().hour >= start_time ) and ( datetime.now().hour <= end_time ):
                cmd_output = check_output( my_cmd, shell = True ) 
                print( cmd_output )
                if debug:
                    print('else' )
