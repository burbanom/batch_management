from read_options import read_options
from batch_management import *

options = read_options('options.yml')
job = BatchScript.from_dict( options = options )
job.ncores = 48
job.nnodes = 3
job.create()
job.submit_job()
print job.job_id
