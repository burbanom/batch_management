#!/usr/bin/env python
"""
Polarizable potential calculation
"""
from __future__ import print_function
import find_files as ff
from pycp2k import CP2K
from ase.io.vasp import read_vasp,read_vasp_out
import re
import mmap
import os
import pandas as pd
import numpy as np
import fnmatch
import gzip
import argparse

def parse_commandline_arguments():
    parser = argparse.ArgumentParser( description = 'cp2k calculator' )
    parser.add_argument( '--ncores', '-nc', metavar = 'N', type=int, required = True, help='set the number of cores to use for this calculation' )
    parser.add_argument( '--path', '-p', metavar = 'S', type=str, required = True, help='Path/folder for the calculations' )
    parser.add_argument( '--results', '-r', metavar = 'S', type=str, required = True, help='Name of the output/results file' )
    parser.add_argument( '--run_types', '-rt', nargs='+', help='list of types of calcs to perform: ENERGY GEO_OPT CELL_OPT', required = True )
    return parser.parse_args()

def clean_files(path,pattern):
  all_files = os.listdir(path)
  filtered = fnmatch.filter(all_files,pattern+"*")
  for element in filtered:
    os.remove(os.path.join(path,element))

def return_value(filename,pattern):
  with open(filename, "r") as fin:
      # memory-map the file, size 0 means whole file
      m = mmap.mmap(fin.fileno(), 0, prot=mmap.PROT_READ)
				    # prot argument is *nix only
      i = m.rfind(pattern)
      m.seek(i)             # seek to the location
      line = m.readline()   # read to the end of the line
  return line.split()[-1]

def vasp_conv(outcar,conv_crit):
    my_forces = outcar.get_forces() 
    conv = np.prod(np.sum(my_forces,axis=1) < conv_crit) 
    return conv 

#===============================================================================
if __name__ == '__main__':
    args = parse_commandline_arguments()
    # Setup calculator
    calc = CP2K()
    calc.working_directory = "./"
    calc.mpi_n_processes = args.ncores
    run_types = args.run_types
    results = args.results

    #===============================================================================
    # Create shortcuts for the most used subtrees of the input.
    CP2K_INPUT = calc.CP2K_INPUT
    GLOBAL = CP2K_INPUT.GLOBAL
    FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
    SUBSYS = FORCE_EVAL.SUBSYS
    MOTION = CP2K_INPUT.MOTION
    FORCEFIELD = FORCE_EVAL.MM.FORCEFIELD

    #===============================================================================
    # FORCE EVAL
    FORCE_EVAL.Method = "FIST"

    root_dir = os.getcwd()
    execfile(root_dir+'/garnets_potential.py')

    spline = FORCEFIELD.SPLINE_add()
    spline.Rcut_nb = 10.5
    spline.Emax_spline = 1000.0

    # Coulomb potential with Ewald summation
    FORCE_EVAL.MM.POISSON.EWALD.Ewald_type = "ewald"
    FORCE_EVAL.MM.POISSON.EWALD.Ewald_accuracy = 1.0E-06 
    FORCE_EVAL.MM.POISSON.EWALD.Rcut = 10.5 
    FORCE_EVAL.MM.POISSON.EWALD.Alpha = 0.3333
    FORCE_EVAL.MM.POISSON.EWALD.Gmax = 13
    FORCE_EVAL.MM.POISSON.EWALD.MULTIPOLES
    FORCE_EVAL.MM.POISSON.EWALD.MULTIPOLES.Max_multipole_expansion = 'DIPOLE'
    FORCE_EVAL.MM.POISSON.EWALD.MULTIPOLES.Pol_scf = 'CONJUGATE_GRADIENT'
    FORCE_EVAL.MM.POISSON.EWALD.MULTIPOLES.Eps_pol = 1.0E-7 
    FORCE_EVAL.MM.POISSON.EWALD.MULTIPOLES.Max_ipol_iter = 100 

    FORCE_EVAL.Stress_tensor = 'ANALYTICAL'

    #################################################
    # The lines below are used to print the dipoles
    #prt_dips = FORCE_EVAL.MM.PRINT.DIPOLES
    #prt_dips.Filename = 'DIPOLES'
    #################################################

    ## Create data frame to hold energies and lattice parameters (for cell_opt)
    indices = []
    my_confs = []
    paths = ff.find_files(root_dir+'/'+args.path,'POSCAR')
    my_cols = ['index']+run_types+['vasp eng. (eV)','a','b','c']
    for path in paths:
      g_number = path.split('/')[-2]
      conf_holder = path.split('/')[-1]
      codes = conf_holder.split('.')
      first_code = codes[1]
      second_code = codes[2]
      my_confs.append(g_number+'-'+second_code)
      indices.append(first_code)

    my_df = pd.DataFrame(index=my_confs,columns=my_cols)
    my_df['index'] = indices

    max_force = 0.00038894615040547636
    ediffg_vasp = 0.02
    conv_line = "reached required accuracy - stopping structural energy minimisation"
    for path in paths:
      os.chdir(path)
      g_number = path.split('/')[-2]
      conf_holder = path.split('/')[-1]
      codes = conf_holder.split('.')
      first_code = codes[1]
      second_code = codes[2]
      config = g_number+'-'+second_code

      outcar_path = ff.find_dirs_files_pattern(path,'OUTCAR*')
      if len(outcar_path) != 0:
	if outcar_path[0][1][-3:] == '.gz':
	  inF = gzip.GzipFile(outcar_path[0][1],'rb')
	  my_outcar = read_vasp_out(inF)
	  converged = vasp_conv(my_outcar,ediffg_vasp) 
	  inF.close()
	else:
	  inF = outcar_path[0][1]
	  my_outcar = read_vasp_out(inF)
	  converged = vasp_conv(my_outcar,ediffg_vasp) 
	if converged:
	    my_df['vasp eng. (eV)'][config] = my_outcar.get_potential_energy()
	else:
	    my_df['vasp eng. (eV)'][config] = np.nan
      else:
	my_df['vasp eng. (eV)'][config] = np.nan



      # Subsys
      my_poscar = read_vasp('POSCAR')
      calc.create_cell(SUBSYS, my_poscar)
      calc.create_coord(SUBSYS, my_poscar)
      SUBSYS.CELL.Periodic = 'XYZ' 
      SUBSYS.CELL.Symmetry = "ORTHORHOMBIC"


      #===============================================================================
      # GLOBAL
      for run in run_types:
	GLOBAL.Run_type = run 
	  #===============================================================================
	  # MOTION
	if GLOBAL.Run_type == 'GEO_OPT':
	  MOTION.GEO_OPT.Type = "MINIMIZATION"
	  #MOTION.GEO_OPT.Max_dr =  1.9E-04
	  MOTION.GEO_OPT.Max_force = max_force
	  #MOTION.GEO_OPT.Rms_dr =  1.9E-04
	  #MOTION.GEO_OPT.Rms_force = 1.9E-04
	  #MOTION.GEO_OPT.Optimizer = 'BFGS'
	  MOTION.GEO_OPT.Optimizer = 'CG'
	  MOTION.GEO_OPT.Max_iter = 1000
	  calc.project_name = "LLZO-geo_opt"
	if GLOBAL.Run_type == 'CELL_OPT':
	  MOTION.CELL_OPT.Type = "GEO_OPT"
	  #MOTION.CELL_OPT.Type = "DIRECT_CELL_OPT" # Tested ths option but gives 'wrong' cell params
	  MOTION.CELL_OPT.Optimizer = "BFGS"
	  MOTION.CELL_OPT.Max_iter = 1000
	  MOTION.CELL_OPT.Keep_symmetry = ".TRUE."
	  ####################################
	  MOTION.GEO_OPT.Type = "MINIMIZATION"
	  #MOTION.GEO_OPT.Max_dr =  1.9E-04
	  MOTION.GEO_OPT.Max_force = max_force
	  #MOTION.GEO_OPT.Rms_dr =  1.9E-04
	  #MOTION.GEO_OPT.Rms_force = 1.9E-04
	  MOTION.GEO_OPT.Optimizer = 'BFGS'
	  MOTION.GEO_OPT.Max_iter = 1000
	  # PRINT
	  my_print = MOTION.PRINT_add()
	  my_print.CELL.EACH.Cell_opt = 1
	  calc.project_name = "LLZO-cell_opt"
	if GLOBAL.Run_type == 'MD':
	  MOTION.MD.Ensemble = "NVE"
	  MOTION.MD.Steps = 0
	  MOTION.MD.Timestep = 1.0
	  MOTION.MD.Temperature = 300
	  # PRINT
	  my_print = MOTION.PRINT_add()
	  my_print.FORCES.EACH.Md = 1
	  my_print.STRESS.EACH.Md = 1
	  my_print.CELL.EACH.Md = 1
	  #################################
	  calc.project_name = "LLZO-NVE"
	if GLOBAL.Run_type == 'ENERGY':
	  calc.project_name = "LLZO-ENERGY"

	clean_files(path,calc.project_name)
	#===============================================================================
	# Run
	calc.run()

	#===============================================================================
	# Let's obtain the final energy of the run 
	eng_string = "ENERGY| Total FORCE_EVAL ( FIST ) energy (a.u.):"
	my_df[GLOBAL.Run_type][config] = return_value(calc.output_path,eng_string)
	if GLOBAL.Run_type == 'CELL_OPT':
	      my_df['a'][config] = return_value(calc.output_path,"CELL| Vector a")
	      my_df['b'][config] = return_value(calc.output_path,"CELL| Vector b")
	      my_df['c'][config] = return_value(calc.output_path,"CELL| Vector c")
    os.chdir(root_dir)
    my_df.to_csv(results, sep='\t')
